from typing import List, Dict, Any

def generate_weekly_reflection(entries: List[Dict[str, Any]]) -> str:
    """Generates an empathetic, non-medical weekly reflection synthesizing emotional trajectory."""
    if not entries:
        return "No journal entries recorded this week. Begin logging daily thoughts to reveal mindful patterns."

    avg_mood = sum(e["mood_score"] for e in entries) / len(entries)
    all_emotions = []
    for e in entries:
        if e.get("emotion_tags"):
            all_emotions.extend([t.strip() for t in e["emotion_tags"].split(",") if t.strip()])

    top_emotions = ", ".join(list(set(all_emotions))[:3]) if all_emotions else "reflective thoughts"

    if avg_mood >= 7.0:
        tone = "You experienced sustained positive momentum this week, with frequent feelings of " + top_emotions + "."
        guidance = "Take time to celebrate these moments of stability and notice what routines supported your energy."
    elif avg_mood >= 5.0:
        tone = "Your week showed a balanced emotional rhythm, navigating both productive days and moments of fatigue."
        guidance = "Consider carving out gentle 10-minute pauses in the afternoon to decompress without screens."
    else:
        tone = "This was a demanding week where things felt heavier than usual."
        guidance = "Remember that difficult emotions are transient. Prioritize restful sleep and be extra compassionate with yourself."

    return (
        f"**Weekly Mindful Reflection (Avg Mood: {avg_mood:.1f}/10)**\n\n"
        f"{tone}\n\n"
        f"**Gentle Inquiry**: {guidance}\n\n"
        f"*[Reminder: MindTrack is a self-reflection tool, not medical advice.]*"
    )
