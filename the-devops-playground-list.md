# The DevOps Playground List  
*40 self-contained adventures that make you dangerously good at real-world infrastructure, automation, and chaos*  
(2025 edition – pick one when you can’t sleep)

1. Build your own “Terraform but tiny” in Python (<500 LOC) that can provision a single EC2 + security group  
2. Write a single-file Kubernetes operator in Go that keeps exactly N replicas of a Deployment alive even if someone deletes them manually  
3. Create a zero-downtime deployment script for any app using only nginx + blue/green directories  
4. Build a self-hosted ngrok alternative with WireGuard peer auto-registration and Cloudflare DNS  
5. Implement a distributed cron using Redis + Lua that survives node failures  
6. Chaos monkey that randomly injects 500 ms latency, packet loss, or kills pods — then auto-heals with Prometheus alerts  
7. GitOps controller in Bash that watches a Git repo and applies raw manifests with kustomize  
8. Tiny CI/CD system using only Git hooks, Docker, and a webhook endpoint (no Jenkins/GitHub Actions)  
9. Prometheus exporter that scrapes your home energy meter / 3D printer / espresso machine  
10. Implement ArgoCD’s application controller logic from scratch in 300 lines (sync loop + diffing)  
11. Build a “kubectl apply” that works over SSH with no kubeconfig on the client  
12. Self-healing etcd cluster in Docker Compose that survives any two nodes dying  
13. Write a Terraform provider for your local coffee shop’s loyalty API (yes, really)  
14. One-line local dev environment that spins up 12 containers with proper networks, volumes, healthchecks, and tears down in 0.2 s  
15. Implement blue/green RDS switch with Route53 weighted records and zero cutover downtime  
16. Create a “git push → production” pipeline that requires exactly two humans to type “LGTM” in a Slack thread  
17. Build a Kubernetes admission webhook that blocks images not signed with cosign  
18. Write a Velero-style backup tool for Kubernetes that only uses rsync + restic  
19. Cross-region PostgreSQL promotion script that works when AWS/GCP goes down in one region  
20. Implement a service mesh sidecar in 100 lines of Rust (just latency injection + retries)  
21. Tiny OpenTelemetry collector that forwards traces from your laptop to a public Honeycomb dataset  
22. Build a “kubectl top” clone that works without metrics-server (using eBPF)  
23. Secrets rotation service that changes database passwords weekly and updates Kubernetes secrets + restarts pods  
24. Implement canary releases using only Istio + Prometheus + a 50-line Python controller  
25. Write a Slack bot that pages the person who broke main — using Git blame + on-call schedule  
26. Local Kubernetes cluster that runs on your Android phone via Termux + k3s  
27. “GitHub Actions but self-hosted” on a Raspberry Pi cluster  
28. Build a policy engine (OPA lite) in <200 lines that enforces “no public buckets” on every deploy  
29. Implement leader election in pure SQLite (for when you can’t use etcd)  
30. Create a “serverless” platform on your homelab using Knative + k3s  
31. Write a tool that converts any Docker Compose file → Kubernetes manifests → Helm chart → ArgoCD Application  
32. Build a Prometheus alert that fires exactly when someone pushes to main on a Friday after 6 PM CET  
33. Implement a “kubectl drain that actually works” — moves PDBs, waits for pod deletion, handles finalizers  
34. Self-hosted certificate authority + step-ca + automatic cert renewal for every service in your homelab  
35. Write a Terraform backend that stores state in an S3 bucket… encrypted with a key from your YubiKey  
36. Build a “kubectl debug” that drops you into a distroless container with all debugging tools injected  
37. Create an eBPF program that blocks Bitcoin miners on your Kubernetes nodes  
38. Implement a GitOps reconciler that works with 5 different Git providers (GitHub, GitLab, Bitbucket, Gitea, Azure DevOps)  
39. Tiny Loki + Promtail that runs in <50 MB RAM and stores one year of your personal logs  
40. “The Final Boss”: a single Makefile that can deploy your entire personal stack (monitoring, backups, VPN, media server, CI, blog) to any cloud with one command

Start with any that makes you whisper “oh that’s evil… I have to try it” at 2 AM.  
You’ll come out the other side understanding infrastructure at a scary depth.

Enjoy the chaos.  
