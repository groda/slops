# ==============================================================================
# BUZZWORD INTERCHANGEABILITY TESTER
#
# This script uses spaCy (a Natural Language Processing library) to test if a
# buzzword within a given text can be replaced by another semantically similar
# buzzword from a predefined list without significantly changing the meaning.
# It highlights the potential for abstract, interchangeable language in
# professional or academic texts.
# ==============================================================================

import spacy          # The primary library for advanced NLP (tokenization, word vectors, etc.)
import sys            # Used for system-specific parameters and functions (though not heavily here)
import random         # Used to randomly select a suitable replacement buzzword
import warnings       # Used to manage Python warnings

# Suppress a common spaCy warning that occurs when a model is loaded without
# full word vectors (like the 'en_core_web_sm' model).
warnings.filterwarnings("ignore", message=r".*The model you're using has no word vectors loaded.*")

# Load the small English spaCy model. This provides essential NLP capabilities
# like tokenization, dependency parsing, and semantic similarity via word vectors.
# Note: The 'sm' (small) model has limited word vectors, impacting similarity accuracy.
nlp = spacy.load("en_core_web_sm")

# --- Configuration: List of Buzzwords and Example Texts ---
# A comprehensive list of common buzzwords and jargon. These are the terms
# the script will look for and use as potential substitutes.
BUZZWORDS = [
    "impact", "innovation", "synergy", "excellence", "sustainability", "leadership",
    "transformation", "empowerment", "collaboration", "alignment", "resilience",
    "efficiency", "scalability", "optimization", "strategy", "engagement",
    "disruption", "enablement", "transparency", "accountability", "agility",
    "visibility", "ideation", "benchmarking", "integration", "streamlining",
    "modernization", "reinvention", "analytics", "deliverables", "capabilities",
    "competencies", "methodologies", "platforms", "ecosystem", "framework",
    "governance", "stakeholders", "paradigm", "milestones", "metrics",
    "insights", "workflow", "pipeline", "holistic approach", "proactive resilience building",
    "strategic mission", "operational priorities", "solutions", "outcomes",
    "alignment", "curation", "synthesis", "orchestration", "acceleration",
    "granularity", "elasticity", "responsiveness", "differentiation",
    "convergence", "expansion", "growth", "scaling", "replication",
    "stewardship", "facilitation", "redeployment", "monetization", "digitalization",
    "iteration", "activation", "implementation", "evaluation", "capacity",
    "enhancement", "stability", "quality", "inclusivity", "accessibility",
    "participation", "coherence", "blueprint", "architecture", "platform", "openness",
    "resilience", "scalability","open science", "responsible research", "artificial intelligence",
    "green transition", "knowledge exchange", "responsible research and innovation"
]

# A list of default multi-line texts to use if the user does not provide input.
# These texts are pre-loaded with several buzzwords for demonstration.
EXAMPLE_TEXTS = ["""“Our long-term vision centers on driving transformation across all business units.
Through continuous transformation initiatives, we aim to build a culture that embraces transformation
as a core organizational value.”
""",

"""The Faculty is committed to fostering excellence in teaching and excellence in interdisciplinary
collaboration to meet future challenges.
""",

"""Research agencies increasingly emphasize innovation as a central criterion in evaluating proposals.
Applicants are expected to demonstrate how their work contributes to innovation within their field and
how planned activities reflect an innovative research culture. Yet the term often appears without a clear
definition, leaving researchers unsure how to articulate innovation in a way that resonates with reviewers.
Our workshop Navigating Innovation examines how funding bodies deploy the concept, how applicants can
meaningfully situate their projects within innovation frameworks, and how innovation narratives can
strengthen the overall structure of a proposal.
""",

"""Our university is committed to generating impact across research,
teaching, and outreach. Departments are encouraged to develop strategies that
maximise impact and demonstrate impact pathways aligned with institutional priorities.
To support this effort, we provide training on crafting convincing impact narratives
at every stage of the research lifecycle.
""",

"""The lab focuses on innovation and excellence in scientific research.
Researchers are encouraged to explore innovative methodologies and document
their innovation outcomes carefully.""",

    """Open Science initiatives are central to our institution's mission.
Faculty and students collaborate to ensure research transparency and accessibility.""",

    """Responsible Research practices are embedded in every project.
Training programs emphasize ethics, reproducibility, and societal impact.""",

"""Our national digital agenda places transformation at the core of future public-service delivery. By cultivating a shared understanding of transformation across agencies, we aim to build interoperable systems that respond more flexibly to citizens’ needs. Transformation, in this sense, is not limited to technical upgrades but extends to a broader cultural readiness to engage with new possibilities.

To secure long-term stability, each ministry will define its own transformation roadmap. These roadmaps will guide investment decisions, inform workforce training goals, and ensure that transformation remains aligned with our overarching commitment to inclusivity and economic competitiveness.
""",

"""This year, we placed renewed emphasis on resilience as a guiding principle across our value chain. By strengthening resilience in our supplier ecosystem and promoting resilience-focused decision-making within our leadership teams, we aim to navigate uncertain economic conditions with greater confidence.

Our forward-looking plan includes embedding resilience metrics into quarterly reviews and ensuring all operational units align with our enterprise-wide resilience framework. This approach allows us to maintain agility, uphold stakeholder expectations, and prepare proactively for emerging challenges.
""",

"""The Future Learning Initiative is grounded in our commitment to academic excellence. Excellence guides our pedagogical choices, shapes curriculum development, and informs our investment in state-of-the-art learning environments. By creating structures that cultivate excellence, we enable students to engage more deeply with complex global issues.

In the coming years, the Initiative will expand interdisciplinary collaborations, strengthen links between research and teaching, and support innovative assessment models. These efforts will ensure that excellence remains central to how our faculty conceptualizes education in an evolving world.
"""
]

# Minimal semantic similarity required (from 0.0 to 1.0) for a buzzword
# to be considered a "plausible" substitute by the spaCy model.
SIMILARITY_THRESHOLD = 0.25

# --- Core Functions ---

def get_semantically_plausible_substitute(original, threshold=0.25):
    """
    Finds a suitable replacement for the 'original' buzzword based on semantic similarity.

    Args:
        original (str): The buzzword to be replaced.
        threshold (float): The minimum similarity score required.

    Returns:
        str: A buzzword from BUZZWORDS that is semantically similar to the original.
    """
    candidates = [bw for bw in BUZZWORDS if bw != original]
    similarities = []

    # Process the original and candidates with spaCy to get word vectors and calculate similarity
    # Note: The similarity calculation relies on the quality of the loaded spaCy word vectors.
    
    # Calculate similarities and filter based on the threshold
    for c in candidates:
        # Calculate cosine similarity between the two buzzwords
        sim = nlp(c).similarity(nlp(original))
        if sim >= threshold:
            similarities.append(c)

    if similarities:
        # Pick randomly among plausible candidates that meet the threshold
        return random.choice(similarities)
    else:
        # Fallback: If no buzzword meets the threshold, pick the one with the highest similarity.
        candidates.sort(key=lambda x: nlp(x).similarity(nlp(original)), reverse=True)
        return candidates[0]


def read_multiline_input():
    """
    Collects multi-line text input from the command line interface (CLI).
    Allows the user to hit Enter for a default text or type 'END' to finish.

    Returns:
        str: The collected multi-line text or a randomly selected example text.
    """
    print("Enter your text (type 'END' on a new line to finish) or hit Enter for default text:")
    
    # Check the first line to handle default text or immediate 'END'
    first_line = input()
    if not first_line or first_line.upper() == "END":
        print("Using one of the default texts.\n")
        return random.choice(EXAMPLE_TEXTS)

    # Initialize the collected text with the first line
    text = first_line + "\n"
    
    # Loop to collect subsequent lines until 'END' is typed
    while True:
        line = input()
        if line.upper() == "END":
            break
        text += line + "\n"

    # Remove the extra newline added after the last collected line
    return text.rstrip("\n")


def find_buzzword(text):
    """
    Searches the input text for the first occurrence of any buzzword from the BUZZWORDS list.
    Supports multi-token buzzwords (e.g., 'open science').

    Args:
        text (str): The text to be scanned.

    Returns:
        str or None: The exact buzzword found (preserving case) or None if none is found.
    """
    text_lower = text.lower()
    for bw in BUZZWORDS:
        if bw.lower() in text_lower:
            # Return the original, properly cased buzzword from the list
            return bw
    return None


def grammatical_substitution(original_text, buzzword, substitute, color=True):
    """
    Performs a case-insensitive replacement of all occurrences of a buzzword
    with the chosen substitute.

    Args:
        original_text (str): The text where substitution will occur.
        buzzword (str): The term to search for and replace.
        substitute (str): The replacement term.
        color (bool): If True, wraps the substitute with ANSI color codes (yellow).

    Returns:
        tuple (str, int): The modified text and the count of substitutions made.
    """
    # ANSI color codes for highlighting
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    count = 0
    text_lower = original_text.lower()
    buzz_lower = buzzword.lower()

    new_text = ""
    i = 0
    # Iterates through the text character by character to find matches
    while i < len(original_text):
        # Check if the lowercased buzzword matches a slice of the lowercased text
        if text_lower[i:i+len(buzz_lower)] == buzz_lower:
            count += 1
            # Apply color if enabled
            replacement = f"{YELLOW}{substitute}{RESET}" if color else substitute
            new_text += replacement
            # Skip past the length of the replaced buzzword
            i += len(buzz_lower)
        else:
            # Copy the original character if no match is found
            new_text += original_text[i]
            i += 1

    return new_text, count


def interchangeable_buzzword_test(text):
    """
    Main logic function that performs the substitution test.

    Args:
        text (str): The input text to be analyzed.

    Returns:
        dict or str: A dictionary containing the test results, or an error string.
    """
    original_buzzword = find_buzzword(text)
    if not original_buzzword:
        return "error: No buzzword found."

    # Get a semantically similar replacement
    replacement = get_semantically_plausible_substitute(original_buzzword)
    
    # Perform the substitution on the original text
    new_text, count = grammatical_substitution(text, original_buzzword, replacement, color=True)

    # Basic syntactic check: checks if the modified text still has a main verb (ROOT)
    # This is a very rough proxy for grammatical coherence/validity.
    parsed = nlp(new_text)
    syntax_ok = any(tok.dep_ == "ROOT" for tok in parsed)

    return {
        "original_buzzword": original_buzzword,
        "replacement_buzzword": replacement,
        "substitution_count": count,
        "text_with_substitution": new_text,
        "syntax_ok": syntax_ok
    }


# --- Script Execution ---

if __name__ == "__main__":
    # 1. Get text input (either user input or a random default text)
    text = read_multiline_input()
    
    # 2. Run the substitution test
    result = interchangeable_buzzword_test(text)

    # 3. Print the results to the user
    print("\n--- Interchangeable Buzzword Test Result ---")
    if isinstance(result, str):
        print(result) # Print error message
    else:
        print(f"original_buzzword: {result['original_buzzword']}")
        print(f"replacement_buzzword: {result['replacement_buzzword']}\n")
        print("Original text:\n")
        print(text, "\n")
        print("Text with substitution:\n")
        print(result["text_with_substitution"])
        print("\nSyntax OK?:", result["syntax_ok"])
