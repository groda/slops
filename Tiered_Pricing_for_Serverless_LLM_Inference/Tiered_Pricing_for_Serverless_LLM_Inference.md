# Reflections on Tiered Pricing for Serverless LLM Inference: A Practitioner’s View

*By groda*

As a Hadoop Administrator who manages clusters on a private cloud, I often think about data locality—the simple but powerful idea that keeping data close to where it’s processed saves time and resources. Hadoop has relied on this principle for years. Lately, I’ve been wondering if the same concept could help solve a growing pain point in serverless AI: the slow startup times when running large language models (LLMs).

Serverless platforms like AWS SageMaker Serverless Inference or Google Cloud Vertex AI are great for cost efficiency—you only pay for what you use. But loading a big model checkpoint (e.g., 130 GB for LLaMA-2-70B) from cloud storage can take over a minute. That’s a problem for anything interactive.

A recent system called **ServerlessLLM** tackles this by keeping model files on the GPU server’s fast local storage (SSD or RAM) and using smarter loading techniques. Startup times drop dramatically—from over 100 seconds to 15–25 seconds or less.

This got me thinking: what if we priced serverless LLM inference based on how fast you want it to start?

### A Simple Three-Tier Idea

- **Cold Start** (base price, e.g., 1 unit per query)  
  The model is fetched from cheap cloud storage like S3 on demand. Slow (~60–120 seconds), but the cheapest option. Fine for occasional or non-time-sensitive queries.

- **Warm Start** (medium price, e.g., 5 units per query)  
  The model is pre-cached on the server’s SSD. Cold starts drop to ~15–25 seconds, and repeated similar queries become much faster thanks to token caching. Good for semi-interactive use cases like customer support bots.

- **Hot Start** (premium price, e.g., 20 units per query)  
  The model lives in the server’s RAM. Cold starts are ~10–15 seconds, and follow-up queries are near-instant. Ideal for real-time applications like live chatbots.

The multipliers (1 / 5 / 20) roughly follow storage cost ratios: cloud object storage is cheap, SSD is several times more expensive per GB, and RAM is the priciest. (RAM prices have also roughly doubled in late 2025 due to AI-driven demand, making the hot tier even more premium.)

### Why This Might Make Sense

Users get choice: pay little and wait, or pay more for speed.  
Providers can better recover the cost of keeping models on expensive local storage.  
It’s transparent—users know exactly what latency they’re buying, unlike today’s opaque internal caching.

Similar tiered approaches already exist elsewhere in cloud pricing (on-demand vs. reserved instances, spot VMs, committed use discounts). This would just apply the same logic to LLM inference latency.

### Closing Thoughts

This isn’t groundbreaking research—just an observation from someone who spends their days keeping big distributed systems running efficiently. I’m sharing it because I believe practical ideas from administrators and operators belong in the conversation too.

The repo with the draft is here: [link to your GitHub repo].  
Feel free to use, ignore, or improve it. No maintenance planned.

*December 2025*