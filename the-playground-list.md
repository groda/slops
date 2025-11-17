# The Playground List
*A Coding Project Collection for the Permanently Curious*  
(2025 edition – 40 self-contained adventures you can start tonight)

Here’s a fresh, practical, and creative list of coding exercises that real developers actually find useful in 2025. They range from beginner-friendly to advanced, cover multiple domains, and are designed to be fun, portfolio-worthy, and immediately applicable in real jobs or open-source.

### Backend / Systems
1. Build a rate-limiter middleware from scratch (token bucket or sliding window) and make it thread-safe/distributed with Redis.
2. Implement a tiny SQLite clone in <1000 LOC (just CREATE TABLE, INSERT, SELECT with B-tree indexing).
3. Write a concurrent web crawler that respects robots.txt and has polite back-off + duplicate detection.
4. Build a distributed lock service using etcd or ZooKeeper (or even PostgreSQL advisory locks).
5. Create a background job system with retries, dead-letter queue, and Prometheus metrics (like Sidekiq but tiny).

### Frontend / Full-stack
6. Implement infinite scroll with virtualized rendering for 100k+ items (React/Virtualizer or Svelte).
7. Build a real-time collaborative rich-text editor using Yjs + WebSockets (no CRDT library allowed at first, then compare).
8. Make a drag-and-drop Kanban board with undo/redo (use Zustand or Redux + immer).
9. Create a “dark mode toggle” that syncs across tabs instantly using BroadcastChannel + localStorage + CSS variables.
10. Build a progressive web app (PWA) that works fully offline for a todo list with sync on reconnect.

### DevOps / Infra-as-Code
11. Write a Terraform module that deploys a highly-available 3-tier app on AWS with zero-downtime blue/green deployments.
12. Create a GitHub Actions matrix workflow that builds and tests your app on 6 different OS/language-version combos and publishes a coverage badge.
13. Build a self-healing Kubernetes operator for a simple CRD (e.g., Memcached cluster that auto-replaces failed nodes).
14. Implement a “chaos monkey” script that randomly terminates pods or delays network traffic and logs how your system recovers.
15. Write a tiny CI/CD system using only Bash, Docker, and Git hooks (for learning how the big ones work).

### Data Engineering / ML
16. Build a real-time analytics dashboard that ingests fake e-commerce events via Kafka → processes with Flink or Spark → serves via Druid or ClickHouse.
17. Create an ETL pipeline that pulls data from 3 public APIs daily, cleans it, and loads into DuckDB + generates a daily email report.
18. Train a tiny LLM (e.g., Phi-3 or Gemma-2B) on your own chat logs or code commits and make it suggest git commit messages.
19. Implement vector search from scratch (HNSW index in pure Python/NumPy) and benchmark against Qdrant or Pinecone.
20. Build a “recommendation as a service” microservice using collaborative filtering with Surprise or implicit.

### Security / Crypto
21. Write a password manager CLI in Rust or Go with Argon2id, ChaCha20-Poly1305, and automatic clipboard clearing.
22. Implement JWT properly (RS256, proper expiration, refresh rotation, revocation list with Redis).
23. Build a secret-sharing scheme (Shamir’s Secret Sharing) and use it to split a private key across 5 friends (3-of-5 to recover).
24. Create a simple zero-knowledge proof demo (e.g., prove you know a hash preimage without revealing it) using circom or gnark.
25. Write a fuzzer for your own JSON API using go-fuzz or hypothesis-python.

### Mobile & Desktop
26. Build a cross-platform desktop app with Tauri that encrypts files in-place using age or Picoclo.
27. Make an Android/iOS app in Flutter or React Native that uses biometric auth + secure enclave/keychain to store a seed phrase.
28. Implement an offline-first notes app with conflict-free merging (Automerge or Yjs).

### Game / Graphics / Creative Coding
29. Code a tiny 3D game engine in Zig or Rust using wgpu (just cubes, camera, and lighting).
30. Build a procedural city generator with L-systems or wave function collapse.
31. Make a shader-only demo in ShaderToy or wgsl that runs at 60 fps on a phone.

### Low-level / Embedded / Performance
32. Write a userspace TCP/IP stack that can ping google.com (like Mike Pound’s series but finish it).
33. Implement a lock-free ring buffer in C11 or Rust and benchmark it with 128 producers/consumers.
34. Port a small program (e.g., cat or ls) to run on WebAssembly and compare performance in-browser vs native.
35. Build a Redis-compatible server that implements GET/SET/INCR/EXPIRE (great systems interview prep).

### Wild but Still Realistic
36. Create a “GitHub bot” that auto-reviews PRs using an LLM and posts polite suggestions.
37. Build a personal telemetry system: collect anonymized data from all your devices → store in TimescaleDB → visualize with Grafana.
38. Make a self-hosted alternative to ngrok using WireGuard + Cloudflare Tunnel.
39. Write a compiler for a tiny language (Brainfuck → x86-64, or a Lisp → WebAssembly).
40. Build “Spotify but local”: scans your music library, generates mood playlists with a tiny ML model, and has a beautiful TUI with ncurses or Ratatui.

Pick any 3–5 of these, finish them properly (tests, CI, README, maybe a live demo), and you’ll have a portfolio that stands out in 2025–2026 job markets across backend, frontend, data, DevOps, or research roles.

