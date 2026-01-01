# JED: The Just Enough Documentation Framework
> *Empowering busy experts by documenting the Delta, not the Standard.*

---

## 1. Introduction
In modern software engineering, documentation often exists in two extremes: a neglected vacuum or an exhaustive, sprawling liability. **Just Enough Documentation (JED)** is a pragmatic middle ground. 

JED recognizes that for a **busy expert**, the most valuable documentation is not a manual of "how to code," but a map of "how to navigate this specific reality." JED prioritizes **onboarding velocity** and **cognitive ease** over sheer volume.

## 2. The Expertise Paradox: General vs. Local Knowledge
A common friction point in high-talent teams is the **"You Should Know" trap**. Out of respect for professional seniority, documentation is often omitted under the assumption that an experienced engineer will intuitively "figure it out."

However, there is a critical distinction to be made:
* **General Expertise:** Understanding the language, the framework, and industry-standard patterns.
* **Local Context:** Understanding a specific project’s unique constraints, legacy decisions, and non-obvious workarounds.

When a project relies too heavily on implied knowledge, it inadvertently creates high barriers to entry. **True "documentation for experts" is the presence of high-density pointers to the unique project context.** JED aims to provide a "fast-pass" that respects an engineer's time by removing the need for software archaeology.

## 3. Philosophy: The Product-Specific Delta ($\Delta$)
The core of JED is shifting focus from documenting everything to documenting only the "surprises." We define this as the **Delta ($\Delta$)**—the difference between a standard implementation and your specific project.

* **The Concept:** A senior engineer possesses **Global Knowledge**. Documentation should only cover **Local Knowledge**.
* **The Formula:** $$Documentation\ Needed = Project\ Reality - Industry\ Standard\ (\Delta)$$



### Identifying the $\Delta$
To keep documentation lean, separate the **Common** from the **Unique**. Only the right-hand column below requires documentation:

| Category | The "Standard" (Don't Document) | The Delta ($\Delta$) (Document This!) |
| :--- | :--- | :--- |
| **Framework** | How React/Python works. | Why a **custom wrapper** is used for all API calls. |
| **Database** | How to write a SQL Join. | Why **JSON blobs** are stored in a relational column. |
| **Architecture** | What a Microservice is. | Why **Service A and B** are tightly coupled. |
| **Deployment** | How Docker works. | The **obscure Env Var** that crashes the build. |

---

## 4. The JED Checklist: Essential Information Items
To satisfy the "Busy Expert" without creating bloat, every project should provide these four pillars, specifically highlighting the $\Delta$ where it exists:

### I. Orientation (The "Big Picture")
* **The Vision Statement:** A single sentence: *"This tool does X for Y so that Z."*
* **The Repository Map:** A directory tree explaining where the core logic, infra, and tests live.
* **The "Rosetta Stone" ($\Delta$):** A list of project-specific terms (e.g., *"In this repo, 'Node' refers to a sensor, not a DOM element"*).

### II. Execution (The "First Hour")
* **The 5-Minute Setup:** A single script or command that leads to a "Success State" (e.g., `./setup.sh`).
* **The Happy Path Example:** A minimal working example that proves the stack is functional.

### III. Strategy & Context (The "Why")
* **Architectural Decision Records (ADRs) ($\Delta$):** Short notes on **why** a non-standard choice was made, preventing the repetition of past mistakes.
* **The Delta Log:** A concise list of where the project deviates from standard framework patterns (the "Surprises").

### IV. Safety (The "Modification Path")
* **Entry Points:** Explicitly naming the main functions or files where execution begins.
* **Definition of Done:** A checklist of required steps before a PR (e.g., "Run linter," "Update version").

---

## 5. Implementation Example: The 5-Minute README
This template serves as the "landing page" for a JED-compliant repository, surfacing the **$\Delta$** immediately.

```markdown
# [Project Name]
> One-sentence Vision: This tool does [X] for [Y] so that [Z].

## 1. Quick Start (5-Minute Setup)

    ./scripts/setup.sh  # Installs dependencies
    npm run dev         # Starts the happy-path example


## 2. The Delta ($\Delta$) (Project Surprises)

If you are an expert in [Primary Stack], this project will feel familiar, EXCEPT:

* **Choice A:** We use [Library X] instead of [Standard Y] because of [Constraint].
* **Choice B:** Data validation is handled in the Controller, not the Model.

## 3. The Rosetta Stone ($\Delta$)

| Term | Local Meaning | Potential Confusion |
| --- | --- | --- |
| **Node** | A physical sensor unit. | Not a DOM node or Node.js. |
| **Session** | 30m of telemetry data. | Not a user login session. |

## 4. Repository Map

* `/src/core`: The business logic (entry point: `index.ts`).
* `/docs/adr`: The "Why" behind our decisions (The ADRs).

## 5. Modification Path (Definition of Done)

1. Run `npm test`.
2. Document any new $\Delta$ in an ADR.
```

---

## 6. Validation: The "Friction-to-Flow" Test
If a project fails these two tests, it is **under-documented**, regardless of the seniority of the engineering team:

1.  **The 15-Minute Wall:** If a competent engineer hits a "dead end" for more than 15 minutes trying to find an entry point or configuration, the **$\Delta$** has not been surfaced.
2.  **The 6-Month Hotfix:** If a busy expert returns to a project after 6 months away, can they ship a critical fix in 30 minutes without external assistance?

---

## 7. Academic Foundations
* **Díaz-Pace, J. A., et al. (2015).** *"Producing Just Enough Documentation: An Optimization Approach."* IEEE Software. 
* **Ambler, S. W. (2002).** *"Agile Modeling: Effective Practices for eXtreme Programming and the Unified Process."* John Wiley & Sons.
* **Hoda, R., et al. (2012).** *"Documentation strategies on agile software development projects."* International Conference on Agile Software Development (XP).

---

## 8. Conclusion
JED is not about a lack of effort; it is about **efficiency**. By focusing on the **Product-Specific $\Delta$**, projects respect both the engineer’s time and the organization’s resources, ensuring that documentation remains a lean, high-value asset rather than a neglected liability. It is important to note that JED is not a license to skip documentation or a justification for the "you should know" mindset; on the contrary, it requires more precision because it demands that we identify and document every friction point where the project deviates from the standard.

When implemented correctly, JED respects the engineer’s time by acting as a **high-speed cache**—allowing them to quickly reload the mental model of a complex system so the real work of engineering can begin.
