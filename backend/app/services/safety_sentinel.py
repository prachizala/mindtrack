import re
from typing import Dict, Any, List

CRISIS_KEYWORDS = [
    r"suicid", r"kill myself", r"end my life", r"want to die",
    r"no reason to live", r"can't go on", r"self harm", r"cut myself",
    r"better off without me", r"hopeless", r"give up on living"
]

VERIFIED_HELPLINES = [
    {
        "name": "Tele-MANAS (Govt. of India National Mental Health Helpline)",
        "number": "14416 / 1800-891-4416",
        "hours": "24/7 Toll-Free",
        "description": "Multi-language confidential mental health tele-counselling service."
    },
    {
        "name": "Vandrevala Foundation Helpline",
        "number": "+91 9999 666 555",
        "hours": "24/7 Free",
        "description": "Professional psychological support and crisis intervention."
    },
    {
        "name": "KIRAN National Mental Health Helpline",
        "number": "1800-599-0019",
        "hours": "24/7 Toll-Free",
        "description": "Government psychological support hotline for distress management."
    },
    {
        "name": "988 Suicide & Crisis Lifeline (International / US)",
        "number": "988",
        "hours": "24/7 Toll-Free",
        "description": "Immediate free and confidential emotional support."
    }
]

NON_MEDICAL_DISCLAIMER = (
    "MindTrack is an emotional well-being self-reflection tool, not a medical or healthcare provider. "
    "It does not provide psychiatric diagnosis, therapy, clinical advice, or crisis intervention."
)

def evaluate_distress_signals(text: str, polarity: float) -> Dict[str, Any]:
    """
    Deterministic, offline crisis sentinel scanner.
    Runs prior to, and independent of, any LLM invocation.
    """
    clean_lower = text.lower()
    matches = []
    for pattern in CRISIS_KEYWORDS:
        if re.search(pattern, clean_lower):
            matches.append(pattern)

    is_distressed = len(matches) > 0 or (polarity <= -0.60)

    return {
        "distress_detected": is_distressed,
        "matched_signals": matches,
        "polarity_score": polarity,
        "non_medical_disclaimer": NON_MEDICAL_DISCLAIMER,
        "helplines": VERIFIED_HELPLINES if is_distressed else []
    }
