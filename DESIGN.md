# Design Specification
## MindTrack: UI/UX & Component System

### 1. Visual Language & Aesthetics
MindTrack is designed around restorative, calming, and emotionally comforting visual principles. It avoids jarring notifications, harsh contrasting borders, and clinical aesthetics.

- **Color Palette**:
  - **Sage Calming Green**: `#10b981` / `#059669` (Positive polarity, primary brand, healing accents)
  - **Warm Sunlight Amber**: `#f59e0b` (Neutral/reflective mood state, gentle prompts)
  - **Soft Sky Indigo**: `#6366f1` (Calm emotional state)
  - **Supportive Coral**: `#f43f5e` (Crisis sentinel indicators, high-distress helpline cards)
  - **Cloud Slate Background**: `#0f172a` (Dark mode) / `#f8fafc` (Light mode)
  - **Surface Container**: `#1e293b` (Elevated card containers)
- **Typography**: Inter + Fraunces / Serif accent for gentle quote headers.

---

### 2. Screen Workflows & Component Hierarchy
1. **Mandatory Header Banner**:
   - Persistent, fixed top disclaimer: *"MindTrack is a self-reflection wellness journal, not a medical or clinical healthcare service."*
2. **Daily Check-In View**:
   - Mood Slider: Interactive 1-10 slider with dynamic organic gradient transition.
   - Emotion Pill Cloud: Multi-select interactive tags (Grateful, Anxious, Energized, Lonely, Productive).
   - Journal Text Area: Clean, distraction-free markdown text editor with auto-save indicator and lock icon indicating *"AES-256 Encrypted"*.
3. **Emergency Crisis Modal**:
   - Renders automatically with gentle, non-threatening phrasing: *"It sounds like things are feeling really heavy right now. You don't have to carry this alone. Free, confidential support is available 24/7."*
   - Cards displaying Tele-MANAS (14416) and Vandrevala Foundation (+91 9999 666 555) with instant tap-to-call links.
4. **Emotional Analytics & Weekly Summary View**:
   - Two dual-axis Recharts graphs tracking Mood (1-10) vs Sentiment Polarity (-1.0 to +1.0).
   - "Weekly AI Mirror": Card presenting gentle observations, recurring positive triggers, and constructive reframing prompts.
