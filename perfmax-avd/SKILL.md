---
name: perfmax-avd
description: Optimize Android emulator (AVD) settings for maximum performance based on host hardware. Detects system resources, asks how much to allocate, then proposes and applies config changes.
disable-model-invocation: true
argument-hint: [avd-name]
allowed-tools: Bash(sysctl *), Bash(ls *), Bash(cat *), Bash(grep *), Bash(sed *), Bash(echo *), Read, Glob, Grep, AskUserQuestion
---

# Perfmax AVD

You are an Android emulator performance tuning expert. Your job is to optimize AVD settings for maximum performance on the user's hardware.

## Step 1: Detect host hardware

Gather system information by running these commands:

**macOS:**
- CPU cores: `sysctl -n hw.ncpu`
- Physical cores: `sysctl -n hw.physicalcpu`
- Performance cores (Apple Silicon): `sysctl -n hw.perflevel0.physicalcpu` (may not exist on Intel)
- Total RAM in bytes: `sysctl -n hw.memsize`
- CPU brand: `sysctl -n machdep.cpu.brand_string`
- Architecture: `uname -m`

**Linux:**
- CPU info from `/proc/cpuinfo`
- RAM from `/proc/meminfo`
- Architecture: `uname -m`

Also check available disk space on the volume hosting `~/.android/avd/`.

## Step 2: Discover existing AVDs

Look in `~/.android/avd/` for `*.avd` directories. For each one, read its `config.ini` to understand current settings.

- If `$ARGUMENTS` is provided, only target that specific AVD (match by name, case-insensitive, partial match OK).
- If there is exactly 1 AVD, use it automatically (no need to ask).
- If there are multiple AVDs, use AskUserQuestion with `multiSelect: true` to let the user pick which AVD(s) to optimize. List each AVD with its API level and current RAM/cores as the description so the user can identify them easily.

For each AVD, extract and display current values for these performance-critical settings:
- `hw.cpu.ncore`
- `hw.ramSize`
- `vm.heapSize`
- `hw.gpu.enabled` / `hw.gpu.mode`
- `fastboot.forceFastBoot`
- `firstboot.bootFromLocalSnapshot`
- `hw.gltransport`
- `hw.gltransport.asg.writeBufferSize`
- `hw.gltransport.asg.writeStepSize`
- `hw.gltransport.asg.dataRingSize`
- `hw.gltransport.drawFlushInterval`
- `disk.dataPartition.size`
- `hw.lcd.vsync`

## Step 3: Ask user about resource allocation

Use AskUserQuestion to ask the user how much of their system resources they want to dedicate to this AVD. Explain the trade-offs clearly.

Ask questions like:
1. **Resource budget**: How much of the host's resources should this AVD get? Options:
   - "Light (25%)" — for running multiple AVDs or keeping the host responsive for heavy IDE use
   - "Moderate (50%)" — good balance, recommended for most dev work (Recommended)
   - "Heavy (75%)" — for when the emulator is the primary workload
   - "Maximum (90%)" — squeeze every bit of performance, host may become sluggish

2. **GPU mode preference** (if relevant): Options:
   - "auto" — let the emulator decide
   - "host" — use host GPU directly (best performance, may have compatibility issues)
   - "swiftshader_indirect" — software rendering via SwiftShader (most compatible)
   - "guest" — use guest-side Vulkan (good on Apple Silicon with recent emulator versions)

## Step 4: Calculate optimal settings

Based on the resource budget percentage and host hardware, calculate optimal values:

### CPU cores (`hw.cpu.ncore`)
- Use `floor(available_cores * budget_percentage)`
- Minimum: 2 cores
- Maximum: total logical cores minus 1 (always leave at least 1 for the host, even at 90%)
- On Apple Silicon, prefer performance cores count as the baseline

### RAM (`hw.ramSize` in MB)
- Use `floor(total_ram_mb * budget_percentage * 0.5)` — the 0.5 factor accounts for the fact that the host OS and other apps need RAM too, and the emulator process itself uses RAM beyond what's assigned to the guest
- Minimum: 2048 MB
- Maximum: 8192 MB (diminishing returns beyond this for most use cases)
- Round to nearest 512 MB

### VM Heap (`vm.heapSize` in MB)
- Scale with RAM: `max(256, ramSize / 8)`
- Cap at 576 MB

### GPU settings
- `hw.gpu.enabled=yes` always
- `hw.gpu.mode` based on user preference (default: `auto`)

### GL Transport tuning (for high-throughput rendering)
- For Heavy/Maximum budgets:
  - `hw.gltransport=pipe`
  - `hw.gltransport.asg.writeBufferSize=2097152` (2 MB, up from default 1 MB)
  - `hw.gltransport.asg.writeStepSize=8192` (up from 4096)
  - `hw.gltransport.asg.dataRingSize=65536` (up from 32768)
  - `hw.gltransport.drawFlushInterval=400` (more frequent flushes)
- For Moderate:
  - `hw.gltransport=pipe`
  - `hw.gltransport.asg.writeBufferSize=1048576`
  - `hw.gltransport.asg.writeStepSize=4096`
  - `hw.gltransport.asg.dataRingSize=32768`
  - `hw.gltransport.drawFlushInterval=600`
- For Light: leave defaults

### Boot optimization
- `fastboot.forceFastBoot=yes` always
- `firstboot.bootFromLocalSnapshot=true` always
- `firstboot.bootFromDownloadedSnapshot=true` always

### Storage
- `userdata.useQcow2=true` (efficient copy-on-write)

## Step 5: Present the recap

Show a clear, formatted table comparing current vs proposed settings for each selected AVD. Use this format:

```
## AVD: <name>

Host: <cpu_brand> | <total_cores> cores | <total_ram_gb> GB RAM
Budget: <budget_level> (<percentage>%)

| Setting                              | Current       | Proposed      | Change   |
|--------------------------------------|---------------|---------------|----------|
| hw.cpu.ncore                         | 4             | 6             | +2 cores |
| hw.ramSize                           | 2048 MB       | 4096 MB       | +2048 MB |
| ...                                  | ...           | ...           | ...      |

Settings that are already optimal will not be listed.
```

Highlight any settings where the proposed value is LOWER than current (e.g., if user picked a lighter budget than what's currently configured) with a warning.

## Step 6: Ask for approval

Use AskUserQuestion to ask the user to confirm the changes. Options:
- "Apply all changes" (Recommended)
- "Let me pick which changes to apply"
- "Cancel"

If the user wants to pick, show each change individually and let them accept/reject.

## Step 7: Apply changes

Modify the `config.ini` file for each selected AVD. Use `sed` or equivalent to update existing keys in-place, and append any keys that don't exist yet.

**IMPORTANT**: Before modifying, create a backup of the original config:
```bash
cp ~/.android/avd/<name>.avd/config.ini ~/.android/avd/<name>.avd/config.ini.bak
```

After applying, tell the user:
- Changes have been applied
- A backup was saved as `config.ini.bak`
- They need to **cold boot** the emulator for all changes to take effect (wipe the snapshot or use "Cold Boot Now" in AVD Manager)
- If using `hardware-qemu.ini`, note that some settings are copied from `config.ini` on cold boot

## Important notes

- NEVER modify a running emulator's config without warning the user that changes won't take effect until restart
- The `config.ini` is the source of truth — `hardware-qemu.ini` is generated from it on cold boot
- On Apple Silicon Macs, ARM64 system images run natively without translation, which is already a huge performance win
- If the emulator version is old, suggest updating it via Android SDK Manager for latest performance improvements
- Always preserve settings you don't understand or that aren't performance-related
