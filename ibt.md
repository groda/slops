# The Interchangeable Buzzword Test  
## A Diagnostic Tool for Detecting Substantive Vacuity in Professional and Institutional Discourse  
### With reference to Harry G. Frankfurt’s On Bullshit (1986/2005)

### Abstract  
This short working paper introduces the Interchangeable Buzzword Test (IBT), a simple heuristic for identifying language that lacks genuine informational or conceptual content. Drawing on Harry G. Frankfurt’s distinction between lying and bullshitting, the IBT posits that a statement or passage is substantively vacuous if its central high-valence term(s) can be replaced by other equally fashionable buzzwords from the same domain while preserving grammatical coherence and apparent meaning. Such interchangeability reveals that the original term functions not as a precise descriptor but as a rhetorical device designed to persuade or impress without regard for truth or specificity—an instance of what Frankfurt calls “bullshit.” Four extended examples from contemporary institutional contexts illustrate the test in action.

### 1. Introduction and Theoretical Foundation  
 
Here is the revised text with repetitions and redundancy eliminated, focusing on a concise explanation of Frankfurt's concept and its direct link to the Buzzword Test:

---

Harry G. Frankfurt's "On Bullshit," a concise philosophical essay originally published in 1986 and expanded into a bestselling book in 2005, explores bullshit as a distinct form of misrepresentation.

Frankfurt, a professor emeritus of philosophy at Princeton University, argues that bullshit is more insidious than outright lying because it involves an **indifference to truth** rather than a deliberate inversion of it. He defines bullshit as speech or writing intended to persuade, impress, or convey a certain image **without any concern for whether it aligns with reality.**

Whereas the **liar** must know the truth in order to conceal it, the **bullshitter** "does not care whether the things he says describe reality correctly. He just picks them out, or makes them up, to suit his purpose" (Frankfurt, 2005, p. 56).

| Form of Misrepresentation | Relationship to Truth | Primary Goal |
| :--- | :--- | :--- |
| **Lying** | Requires knowledge of the truth to subvert it. | Conceal the truth. |
| **Bullshitting** | Total indifference to whether the statement is true or false. | Achieve a desired effect on the audience. |

Frankfurt posits that bullshit proliferates in modern society due to demands for opinions on complex topics and contexts (like advertising, politics, or academia) where sincerity is secondary to persuasion. Modern professional and academic discourses, where participants must speak authoritatively about complex matters, are particularly fertile ground.

### Connection to the Interchangeable Buzzword Test

This framework directly ties into the "Interchangeable Buzzword Test," which exposes a key mechanism of modern bullshit. **Buzzwords**—terms that sound weighty but carry multiple, shifting, or deliberately vague meanings—serve as ideal vehicles for this type of discourse.

The test demonstrates that texts laden with vague, semantically substitutable terms (like "innovation" or "impact") lack genuine substance. Frankfurt's framework would classify such writing as bullshit because the language is crafted to persuade reviewers (e.g., in funding proposals) or sound impressive, without a genuine commitment to conveying accurate or meaningful information. The interchangeable nature of the jargon reveals that these terms add no irreplaceable semantic content.

### 2. Formal Statement of the Interchangeable Buzzword Test (IBT)  
A passage fails the IBT—and may therefore be classified as substantively vacuous—if the following operation can be performed:  

Replace every occurrence of its primary high-valence buzzword (or short buzz-phrase) with one or more alternative buzzwords from the same register, and the resulting text

(a) remains grammatically correct, (b) retains the same rhetorical tone and persuasive force, and (c) conveys an equivalently vague or generic proposition.

### 3. Extended Examples

**Example 1 – EU Research Funding Discourse**  
Original (Horizon Europe style):  
“The proposed action will deliver transformative impact by addressing grand societal challenges through disruptive innovation and responsible research and innovation principles.”  

Interchange 1 (“transformative impact” → “game-changing excellence”; “disruptive innovation” → “breakthrough discovery”):  
“The proposed action will deliver game-changing excellence by addressing grand societal challenges through breakthrough discovery and responsible research and innovation principles.”  

Interchange 2 (“responsible research and innovation” → “mission-oriented approach”):  
“The proposed action will deliver game-changing excellence by addressing grand societal challenges through breakthrough discovery and mission-oriented approach principles.”  

The sentence survives multiple substitutions without loss of apparent meaning, revealing that none of the highlighted terms carries unique descriptive weight.

**Example 2 – University Strategic Plan**  
Original:  
“Our institution is committed to fostering inclusive excellence and advancing interdisciplinary collaboration in order to become a global leader in sustainable innovation.”  

Interchange (“inclusive excellence” → “equitable distinction”; “interdisciplinary collaboration” → “cross-boundary synergy”; “sustainable innovation” → “resilient transformation”):  
“Our institution is committed to fostering equitable distinction and advancing cross-boundary synergy in order to become a global leader in resilient transformation.”  

The revised version could appear in the next university’s strategic plan with no one noticing the difference.

**Example 3 – Corporate ESG Report**  
Original:  
“Through stakeholder capitalism and circular economy principles we create shared value and drive long-term sustainable growth for all our stakeholders.”  

Interchange (“stakeholder capitalism” → “conscious leadership”; “circular economy” → “regenerative business”; “shared value” → “triple bottom line impact”; “sustainable growth” → “inclusive prosperity”):  
“Through conscious leadership and regenerative business principles we create triple bottom line impact and drive long-term inclusive prosperity for all our stakeholders.”  

The substitution yields a text that is functionally identical in its persuasive emptiness.

**Example 4 – National Science Policy Document**  
Original:  
“Frontier research and curiosity-driven basic research are essential to achieving scientific breakthroughs and maintaining technological sovereignty in an era of strategic autonomy.”  

Interchange (“frontier research” → “moonshot science”; “curiosity-driven basic research” → “blue-sky exploration”; “scientific breakthroughs” → “paradigm-shifting advances”; “technological sovereignty” + “strategic autonomy” → “innovation leadership” + “resilient capability”):  
“Moonshot science and blue-sky exploration are essential to achieving paradigm-shifting advances and maintaining innovation leadership in an era of resilient capability.”  

Even with four compounded substitutions, the passage still reads as authoritative policy rhetoric.

### 4. Conclusion  
The Interchangeable Buzzword Test offers a quick, reproducible method for detecting Frankfurtian bullshit in institutional language. When a text passes the test—i.e., when its core terms prove mutually replaceable without damage to its rhetorical function—it demonstrates that those terms serve not to inform but to perform. In an age that demands constant articulation of vision, strategy, and impact, the test reminds us that clarity and precision remain the only reliable antidotes to indifference toward truth.

### 5. Source Code

The full source code for the **Interchangeable Buzzword Tester** is provided below for transparency and replication.

[**Download the `ibt.py` script here**](ibt.py).

#### How to Run `ibt.py`

Your script is run directly from the **Command Line Interface (CLI)**.


Open your terminal, navigate to the script's directory, and run:

```bash
python ibt.py
```

The script will prompt you: 

`Enter your text (type 'END' on a new line to finish) or hit Enter for default text:`


| Action | Result |
| :--- | :--- |
| **Press Enter immediately** | Uses a **random default text** for analysis. |
| **Type text, then `END`** | Analyzes your **custom text**. |

The script outputs the result, highlighting the **original buzzword** (e.g., *efficiency*) and its **semantically similar replacement** (e.g., *optimization*) within the text.

**Example Input:**

```
We must focus on efficiency to improve scalability.
END
```

**Example Output:**

```
original_buzzword: efficiency
replacement_buzzword: optimization
...
Text with substitution:
We must focus on optimization to improve scalability.
```

### Reference  
Frankfurt, Harry G. (2005). On Bullshit. Princeton University Press. (Original essay published 1986 in Raritan Quarterly Review.)
