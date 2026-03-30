# Pathscan
Lightweight multithreaded web directory and endpoint scanner.

Designed for reconnaissance, it scans a target for common sensitive paths
including admin panels, configuration files, backups, APIs, and debug endpoints.
It highlights interesting HTTP responses (200, 403, redirects, 5xx) and filters
duplicate responses to reduce noise.

Useful for CTFs, bug bounty recon, and quick surface mapping.
