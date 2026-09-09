# Linux OS — Software Features

## Kernel & Architecture
- Monolithic kernel with loadable modules — core OS is fast, but drivers can be added/removed without rebooting
- Preemptive multitasking and multi-core (SMP) support
- cgroups and namespaces for process isolation — the foundation of containers like Docker

## File Systems
- Multiple native file systems: ext4 (standard), Btrfs (snapshots/compression), XFS (high performance), ZFS (enterprise)
- Can read/write many formats including NTFS and exFAT
- Journaling support prevents data corruption on unexpected shutdowns

## Security
- Mandatory Access Control via SELinux or AppArmor — restricts what processes can do even as root
- Full disk encryption via LUKS/dm-crypt
- Seccomp syscall filtering and ASLR memory protection built in
- Open source — vulnerabilities are found and patched quickly by the community

## Networking
- Full IPv4/IPv6 stack with powerful firewall tools (nftables/iptables)
- WireGuard VPN built directly into the kernel
- Advanced traffic shaping and network namespaces for containers

## Process & Memory Management
- Virtual memory with demand paging — memory is only loaded when needed
- Copy-on-Write forking saves memory when spawning new processes
- OOM (Out of Memory) killer manages memory pressure automatically

## Virtualisation & Containers
- KVM hypervisor built into the kernel — used by most cloud providers
- Native container support via cgroups/namespaces — Docker runs with no overhead
- VFIO allows direct GPU/PCI passthrough to virtual machines

## Package Management
- Centralised package managers (apt, pacman, dnf) manage software and dependencies
- Universal formats: Flatpak, Snap, AppImage for cross-distro apps
- Everything updated through one consistent system — no hunting for installers

## Desktop & Graphics
- Supports both X11 and Wayland display servers
- Highly customisable — desktop environments, compositors, and window managers are all swappable
- Vulkan and OpenGL support via open-source Mesa drivers
- Gaming via Proton/Wine compatibility layer

## System Control
- Full user control — every layer of the OS is replaceable
- No forced updates or mandatory telemetry
- Completely open source and auditable
