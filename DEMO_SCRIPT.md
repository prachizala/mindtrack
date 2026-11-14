# MindTrack: 3-Minute Video Demo Script

**Speaker**: Prachi Zala  
**Target Audience**: Technical Recruiters, Ethics Evaluators  

### [00:00 - 00:30] Privacy in Mental Health Apps
"Hello! I'm Prachi Zala. Millions of people want to journal their personal thoughts, but fear cloud data breaches. Moreover, unregulated AI mental health apps often attempt pseudo-medical diagnoses without crisis protection. MindTrack was built with a privacy-first, safety-first architecture."

### [00:30 - 01:30] Client-Side AES-256 Encryption
"When I write a journal entry, watch what happens in the database: the raw journal body is immediately encrypted using AES-256 via Fernet before touching the disk. If a hacker inspects our SQLite database, they only see random ciphertext blobs. The decrypted text is only viewable by the authenticated user."

### [01:30 - 02:30] Safety Sentinel & Helplines
"Most importantly, our app includes a deterministic Safety Sentinel. Notice our persistent top disclaimer: MindTrack is not medical advice. If an entry exhibits acute distress, our offline regex sentinel immediately triggers a modal with verified 24/7 helplines like Tele-MANAS and Vandrevala Foundation."

### [02:30 - 03:00] Stack & Reliability
"Built with FastAPI, Cryptography, and Recharts, backed by 100% passing pytest suites. Thank you!"
