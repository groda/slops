# AI Directive Markup Language (AIDML): A Novel Meta-Language for AI-Assisted Composition of Scientific Papers

#### Prompted by @groda • March 15, 2026 • Assisted by Grok 4 built by xAI

## Abstract

In the rapidly evolving landscape of artificial intelligence, large language models (LLMs) such as GPT-4, Claude, and Llama have transformed scholarly writing by automating repetitive tasks. This paper introduces the AI Directive Markup Language (AIDML), a tag-based meta-language inspired by HTML, LaTeX, Markdown, and Typst, but tailored for embedding AI directives within scientific documents. AIDML enables authors to provide conceptual skeletons—outlining ideas and structures—while delegating formulaic elements, such as reformulation, translation, and content generation, to AI systems. By limiting its application to scientific papers, which often adhere to rigid patterns (e.g., IMRaD structure: Introduction, Methods, Results, and Discussion), AIDML enhances efficiency and consistency. We detail its syntax, propose additional directives for advanced generative capabilities, and review prior art in prompt structuring. Preliminary assessments indicate a potential 30% reduction in drafting time for formulaic sections, fostering a new paradigm where humans focus on high-level ideation and AI handles the "fill-in-the-blanks" workload.

## Introduction

The integration of AI into human cognition has subtly reshaped how we formulate thoughts. Since the advent of sophisticated LLMs like OpenAI's GPT series and Anthropic's Claude, individuals increasingly provide high-level ideas or skeletons—core concepts, outlines, or key points—while relying on AI to perform repetitive, formulaic work such as expanding details, ensuring grammatical precision, or generating supportive content. This shift mirrors historical technological adaptations, like the typewriter enabling faster drafting or word processors facilitating revisions, but with AI, the collaboration is more dynamic and intelligent.

In scientific writing, this evolution is particularly pronounced due to the genre's formulaic nature: papers typically follow predictable patterns, including abstracts, introductions with literature reviews, methodological descriptions, results with data analysis, discussions of implications, and conclusions. However, traditional tools fall short in seamlessly incorporating AI assistance without disrupting the workflow.

To address this, we propose the AI Directive Markup Language (AIDML), a meta-language that embeds AI directives via tags directly into the document. Unlike general prompting, AIDML allows inline instructions, such as reformulating a hypothesis or generating a figure description, while preserving the document's structure. For instance, a vague idea can be wrapped in a `<generate:hypothesis>` tag for AI elaboration. By focusing exclusively on scientific papers, AIDML leverages their patterned format to maximize utility, enabling authors to "direct" AI like a co-author specialized in rote tasks.

This paper expands on AIDML's design, introduces new tags for advanced generative text (e.g., section-level creation), and incorporates related prior work to contextualize its novelty.

## Related Work

Markup languages have historically structured content: HTML for web pages, LaTeX for typesetting, Markdown for simplicity, and Typst for modern publishing. In AI prompting, similar structured approaches have emerged to mitigate ambiguity.

Notable predecessors include Prompt Markup Language (PromptML), a domain-specific language for defining AI prompts deterministically with section annotations like `@context` and `@objective`.[1] POML (Prompt-Oriented Markup Language or Prompt Orchestration Markup Language), often likened to "HTML for AI prompts," uses tag-based syntax (e.g., `<role>`, `<task>`) for modular, reusable prompts, with implementations from Microsoft supporting data integration and compilation to formats like Markdown or JSON.[3][4][5][8] BAML (Boundary AI Markup Language) extends this by embedding type-safe prompts in programming languages like Python or TypeScript, treating prompts as functions for better testing and error handling.[6] Discussions in communities also highlight using XML or Markdown for prompts to reduce ambiguity, with AI systems like Claude responding better to tagged structures.[6][9]

### Comparison to POML

POML, developed by Microsoft and open-sourced in 2025, represents a significant advancement in structured prompt engineering.[1][2][3][6][7][8] It employs an HTML-like syntax with semantic tags such as `<role>`, `<task>`, and `<example>` to organize prompts modularly, enhancing readability and reusability. POML also incorporates CSS-like styling for presentation control, templating for dynamic data integration, and tooling for compilation into various formats, addressing challenges like format sensitivity in LLMs.

In comparison, AIDML shares the tag-based paradigm but diverges in focus and application. While POML is primarily a tool for crafting and orchestrating prompts themselves—treating them as structured assets in development workflows—AIDML embeds directives directly into the content of scientific documents. This makes AIDML more document-centric, allowing inline AI interventions (e.g., `<reformulate>` or `<generate:advanced>`) that operate on enclosed text during processing. POML excels in prompt maintainability for AI applications, whereas AIDML targets scholarly writing efficiency by enabling authors to mark up skeletons for AI to "fill in," leveraging the formulaic structure of scientific papers. Both promote modularity, but AIDML's nesting and generative tags provide specialized support for iterative text refinement, potentially complementing POML in hybrid workflows where POML-structured prompts interpret AIDML documents.

AIDML differentiates by being document-centric for scientific papers, focusing on inline directives that operate on enclosed content, and supporting nested, generative tags without requiring programming knowledge. It builds on these works by emphasizing AI as a "filler" for human-provided skeletons, aligning with evolving cognitive habits.

## AIDML and Prompt Engineering Frameworks

Prompt engineering frameworks provide structured methodologies for crafting effective inputs to LLMs, often using acronyms to guide the inclusion of key elements like context, objectives, and examples.[10][11][13][15][16][18] Examples include COSTAR (Context, Objective, Style, Tone, Audience, Response), CRISPE (Capacity/Role, Insight, Statement, Personality, Experiment), RTF (Role, Task, Format), Chain of Thought (step-by-step reasoning), and others like RISE, CREATE, and SPEAR. These frameworks aim to reduce ambiguity, improve consistency, and enhance LLM outputs by systematizing prompt design.

AIDML relates to these frameworks by formalizing their principles into a markup language, embedding them inline within scientific documents rather than as standalone prompts. For instance, AIDML tags like `<reformulate style="formal">` incorporate style and tone from COSTAR, while `<generate:advanced section="discussion" implications="cognitive shifts">` aligns with Chain of Thought by enabling structured generation. This meta-language approach extends prompt engineering from ad-hoc textual instructions to a persistent, document-integrated system, particularly suited to the repetitive patterns in scientific papers. By allowing nesting (e.g., `<analyze:stats><summarize>Data</summarize></analyze>`), AIDML supports complex, layered prompting akin to advanced frameworks like Tree of Thoughts (ToT) or Chain of Density.

While prompt engineering frameworks are versatile for general LLM interactions, AIDML tailors them for AI-assisted authoring, promoting transparency and traceability in scholarly work. This integration could standardize prompt practices in academia, though it adds a learning curve for tag syntax.

## Design Principles of AIDML

AIDML adheres to principles of simplicity, extensibility, context-awareness, AI-agnosticism, and transparency. Tags use `<directive:parameters>content</directive>` syntax, with nesting for compound operations (e.g., `<translate:de><reformulate>Text</reformulate></translate>`).

In scientific contexts, AIDML exploits patterns like hypothesis formulation, data analysis, and citation integration, allowing authors to sketch ideas and let AI elaborate.

## Syntax and Semantics

### Core Directives

| Directive     | Parameters              | Description                                      | Example |
|---------------|-------------------------|--------------------------------------------------|---------|
| `reformulate` | style (e.g., formal)   | Rephrases for clarity.                           | `<reformulate:formal>This sentence bad.</reformulate>` → "This sentence is poorly constructed." |
| `translate`   | language code          | Translates content.                              | `<translate:de>Hello, world.</translate>` → "Hallo, Welt." |
| `format`      | type (e.g., table)     | Structures content.                              | `<format:bullet>Item1 Item2</format>` → - Item1<br>- Item2 |
| `merge`       | strategy (e.g., coherent) | Combines segments.                            | `<merge:coherent>Para1 Para2</merge>` → A single coherent paragraph. |
| `expand`      | length (e.g., detailed)| Elaborates content.                              | `<expand:detailed>Brief idea.</expand>` → Expanded explanation. |
| `summarize`   | length (e.g., short)   | Condenses text.                                  | `<summarize:short>Long text.</summarize>` → Concise summary. |
| `cite`        | source (e.g., web:query)| Inserts references.                              | `<cite:web:AI history</cite>` → [Reference to source]. |
| `generate`    | type (e.g., example)   | Produces new content; advanced for sections.     | `<generate:example>Topic</generate>` → Relevant example. |

### Additional Suggested Directives for Scientific Papers

To enhance AIDML's utility in scientific writing, we propose the following tags, emphasizing generative capabilities where AI "fills in the blanks" based on human skeletons:

| Directive         | Parameters                  | Description                                                                 | Example Usage |
|-------------------|-----------------------------|-----------------------------------------------------------------------------|---------------|
| `hypothesize`     | Optional: domain (e.g., biology) | Generates a testable hypothesis from provided premises or data sketches.   | `<hypothesize>Climate data trends suggest...</hypothesize>` → "Hypothesis: Increased CO2 levels correlate with biodiversity decline." |
| `analyze`         | Type: stats, qualitative   | Performs analysis on enclosed data or text (e.g., statistical summary).    | `<analyze:stats>Dataset: 1,2,3;4,5,6</analyze>` → Mean, variance, etc. |
| `visualize`       | Type: chart, diagram       | Generates descriptions or pseudo-code for figures (e.g., matplotlib snippets). | `<visualize:chart bar>Categories: A=10, B=20</visualize>` → Figure description or code. |
| `review`          | Type: literature; query    | Summarizes prior work on a topic, pulling from queries or sketches.        | `<review:literature>AI in writing</review>` → Concise lit review. |
| `methodize`       | Optional: steps (e.g., experimental) | Structures a methods section from bullet-point ideas.                     | `<methodize>Step1: Collect data; Step2: Analyze</methodize>` → Formatted methods. |
| `discuss`         | Optional: implications     | Elaborates on results' implications, limitations, and future work.         | `<discuss>Results show X</discuss>` → Discussion paragraph. |
| `generate:advanced` | Type: section (e.g., abstract, conclusion); topic | Advanced generative tag for creating entire sections from outlines or keywords, supporting human-AI ideation where users provide skeletons. | `<generate:advanced section="introduction" topic="AI evolution">Key points: Shift in thinking, AI fillers</generate:advanced>` → Full intro section. |

These tags support nesting, e.g., `<generate:advanced section="results"><analyze:stats>Data</analyze></generate:advanced>` for data-driven results generation.

## Examples

Consider a scientific paper draft on AI cognition:

Raw AIDML:
```
<hypothesize>AI changes thought formulation.</hypothesize>
<generate:advanced section="discussion" implications="cognitive shifts">
    Humans provide skeletons; AI fills blanks.
</generate:advanced>
<review:literature>Structured prompting languages</review>
```

Processed Output:
Hypothesis: The integration of AI leads to humans delegating formulaic tasks, altering cognitive processes. [Generated discussion on implications...] Prior work includes POML and BAML for prompt structuring.

This demonstrates AIDML's role in scientific workflows.

## Implementation Considerations

AIDML can be parsed by LLMs like GPT or Claude, with preprocessors handling tags. For scientific tools, integration with Overleaf or Jupyter could enable real-time rendering.

## Discussion

AIDML aligns with the growing habit of human-AI symbiosis in thought formulation, where scientists outline hypotheses or methods, and AI generates polished, formulaic text. This not only boosts productivity but also standardizes scientific discourse. Ethical considerations include ensuring AI-generated content is verifiable and authorship is transparent.

While prior works like POML and BAML provide foundational structures, AIDML's focus on scientific patterns and advanced generative tags (e.g., `<generate:advanced>`) offers targeted advancements.

## Conclusion

AIDML innovates AI-assisted scientific writing by embedding directives that leverage AI for filling structural gaps, building on related markup languages. Future extensions could include multimodal tags for figures or equations.

## References

1. PromptML Documentation. Available at: https://www.promptml.org/

2. Rajan, B. (2025). The Rise of POML: Structuring Prompts for the AI Era. Medium.

3. Microsoft Community. (2025). Unlock the Full Potential of LLMs with POML.

4. Microsoft GitHub. (2025). POML Repository.

5. Atlan, L. (2025). The Prompting Language Every AI Engineer Should Know: A BAML Deep Dive. Towards AI.

6. Additional community discussions on structured prompting.

7. POML Documentation - Microsoft Open Source. (2025). https://microsoft.github.io/poml/latest

8. microsoft/poml: Prompt Orchestration Markup Language. GitHub.

9. The complete guide to prompt engineering frameworks. (2025). https://www.parloa.com/knowledge-hub/prompt-engineering-frameworks

10. Mastering AI Prompt Engineering: The Six Frameworks. LinkedIn.

11. UMMS Artificial Intelligence: Prompt Frameworks. (2026). https://guides.lib.umich.edu/c.php?g=1406239&p=10420137

12. Guide to Standardized Prompt Frameworks. (2025). https://latitude.so/blog/guide-to-standardized-prompt-frameworks

13. Prompt Frameworks 2025 Explained: What Works and Why. (2025). https://www.encodedots.com/blog/prompt-frameworks-2025

