# Changes Log - MindTrack

## Work Package 5: Boilerplate Repos and Profile Review

### Summary of Changes
1. **README.md Deprecation & Supersession Notice**:
   - Added prominent banner at the very top of `README.md`:
     `> **Note:** This backend prototype has been integrated and superseded by our full-stack Streamlit NLP suite [MindPulse: Mood Tracker & Sentiment Analysis](https://github.com/prachizala/mood-tracker-sentiment-analysis). Kept here as an API reference.`
   - Maintained full architectural details, zero-knowledge AES-256 field encryption specs, deterministic crisis sentinel details, API endpoints table, and local run/test instructions.
2. **CI & Pytest Configuration**:
   - Added `pytest.ini` with `pythonpath = backend` for seamless root-level pytest execution.
   - Refined `.github/workflows/ci.yml` to trigger on `push` (including `review-fixes`) and `pull_request`.
3. **Verification & Tests**:
   - Ran `pytest backend/tests/test_mindtrack.py` locally: 7 passed out of 7 tests.

### Items Skipped & Rationale
- **Repository Deletion**: Did NOT delete the repository per explicit instructions. The codebase is preserved intact as a reference prototype for encrypted REST API architectures.

### Recommendations for Prachi
- **Archive on GitHub**: It is strongly recommended to navigate to **GitHub Repository Settings > Danger Zone > Archive this repository** and mark `mindtrack` as **Archived (Read-Only)**.
  - *Rationale*: Marking this prototype repository as archived clarifies for recruiters and visitors that your active flagship platform for mental wellness and sentiment analysis is `mood-tracker-sentiment-analysis` (MindPulse), preventing profile clutter and redundant repository confusion.
