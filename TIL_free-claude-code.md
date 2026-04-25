**Today I learned about a GitHub project: [free-claude-code](https://github.com/Alishahryar1/free-claude-code)**

It lets you use **Claude Code** (the official Anthropic CLI + VSCode extension) completely for free by rerouting its requests to other models instead of Anthropic’s paid API.

At first glance it feels a lot like LiteLLM proxy — the idea is to reroute your queries to different services — but it’s actually quite different. While LiteLLM is a general-purpose gateway for any app, `free-claude-code` is a **specialized proxy** built specifically so the real Claude Code tool works without an Anthropic key.

### How it works (super simple)

1. You run this proxy locally (`http://localhost:8082` by default).  
2. You point Claude Code at it instead of Anthropic’s real endpoint (by setting `ANTHROPIC_BASE_URL=http://localhost:8082`).  
3. Claude Code still thinks it’s talking to real Claude (it sends normal Anthropic Messages API requests in SSE format).  
4. The proxy intercepts those requests and **forwards/reroutes** them to whichever backend you configured in your `.env` (NVIDIA NIM free tier, OpenRouter, DeepSeek, LM Studio, llama.cpp, etc.).

It even supports per-model routing, so you can map “Opus” to a strong model on NVIDIA, “Sonnet” to another, and “Haiku” to something cheap and fast.

### Fully offline with local models

**Yes — it works excellently with local models.**  
`free-claude-code` has **built-in, first-class support** for fully offline/local inference. You don’t need any cloud API keys at all.

Supported local backends:
- **LM Studio** (recommended for most people) — Base URL: `http://localhost:1234/v1`
- **llama.cpp** (lighter, runs `llama-server`) — Base URL: `http://localhost:8080/v1`

Both are OpenAI-compatible `/v1` endpoints, and the proxy translates Claude’s Messages API perfectly to them.

In your `.env` file you just do something like:

```dotenv
# LM Studio example
LM_STUDIO_BASE_URL="http://localhost:1234/v1"
MODEL_OPUS="lmstudio/your-model-here"
MODEL_SONNET="lmstudio/your-model-here"
MODEL_HAIKU="lmstudio/your-model-here"

# OR llama.cpp example
LLAMACPP_BASE_URL="http://localhost:8080/v1"
MODEL_OPUS="llamacpp/local-model"
MODEL_SONNET="llamacpp/local-model"
```

Then just run the proxy and point Claude Code to `http://localhost:8082` like normal. Everything stays 100% offline. Streaming and thinking tokens work great.

**What about Gemma?**  
**Yes, Gemma works too** (including Gemma 3 and Gemma 4 variants).  
The proxy doesn’t list Gemma by name in the README, but that’s because it supports **any GGUF model** you load into LM Studio or llama.cpp.

Just download a Gemma GGUF from Hugging Face, load it in LM Studio (or run with `llama-server`), and use the exact model identifier shown in the UI.

Example for LM Studio:
```dotenv
MODEL_OPUS="lmstudio/google/gemma-3-27b-it-GGUF"
MODEL_SONNET="lmstudio/google/gemma-3-27b-it-GGUF"
MODEL_HAIKU="lmstudio/google/gemma-3-9b-it-GGUF"
```

To put this into perspective, here’s a **clean, up-to-date comparison table of the major LLM gateways in 2026**:

| Gateway              | Open Source? | Self-Hosted? | Primary Language | Best For                              | API Formats Supported                  | Provider / Model Count | Latency Overhead          | Key Superpowers                              | Claude Code / Anthropic Support | Pricing (2026)                  |
|----------------------|--------------|--------------|------------------|---------------------------------------|----------------------------------------|------------------------|---------------------------|----------------------------------------------|---------------------------------|---------------------------------|
| **free-claude-code** | Yes         | Yes         | Python          | Free/cheap Claude Code (CLI + VSCode) | Anthropic Messages only                | ~5 (NIM, OpenRouter, DeepSeek, local) | Very low                 | Dead-simple setup for Claude Code, free NIM tier | ★★★★★ (built for it)          | Completely free                |
| **LiteLLM**          | Yes         | Yes         | Python          | Developer-first general proxy         | OpenAI + 100+ others (translates)      | 1,600+ models         | Moderate (~10-50ms)      | Massive provider list, easiest to start      | ★★★★ (via config)              | Free (self-hosted)             |
| **Portkey**          | Yes         | Yes + Cloud | Python/TS       | Production + enterprise governance    | OpenAI, Anthropic, custom              | 1,600+ models         | 20-40ms                  | Guardrails, caching, budgets, MCP, observability | ★★★★★                          | Free tier + paid plans         |
| **Helicone**         | Yes         | Yes + Cloud | Rust            | Observability-first teams             | OpenAI + Anthropic                     | 100+                   | ~8ms                     | Best logging + caching, very lightweight     | ★★★★                           | Free (self-hosted)             |
| **Bifrost (Maxim AI)** | Yes       | Yes         | Go              | High-performance production           | OpenAI, Anthropic, Bedrock, etc.       | 20+ providers         | ~11µs (insanely fast)    | Lowest latency, semantic caching, enterprise | ★★★★★                          | Free (self-hosted)             |
| **Kong AI Gateway**  | Yes         | Yes         | Lua/Go          | Teams already using Kong/K8s          | OpenAI + Anthropic + plugins           | Broad                  | Low                      | Full API management + AI plugins             | ★★★★                           | Free (open-source)             |
| **Cloudflare AI Gateway** | No     | Cloud       | —               | Edge + serverless apps                | OpenAI + Anthropic                     | 20+                    | Very low (edge)          | Global edge network, caching, rate limiting  | ★★★★                           | Pay-per-use (cheap)            |
| **OpenRouter**       | No          | Cloud       | —               | Easy multi-model access (no accounts) | OpenAI-compatible + Anthropic          | 500+ models           | Low                      | Huge catalog + smart routing/fallbacks       | ★★★★ (very popular for Claude Code) | Pay-per-token + free tier     |

### Quick recommendations
- **Just want Claude Code for free** → go with **free-claude-code** right now. It’s the cleanest and most targeted solution (especially if you want to run everything locally with models like Gemma).
- **Need a general-purpose proxy** → LiteLLM or Bifrost.
- **Production/team usage** (costs, guardrails, observability) → Portkey or Helicone.
- **Maximum model variety with zero setup** → OpenRouter (many people even use it as the backend for free-claude-code).

Super handy little project if you’re tired of paying for Claude API tokens just to use the official coding tools!
