**Persona-Driven Document Intelligence**
**Adobe India Hackathon – Round 1B**  
**Theme**: “Connect What Matters — For the User Who Matters”

## 💡 Challenge Overview
This project presents an intelligent system that analyzes a collection of documents and extracts the most relevant sections tailored to a specific **persona** and their **job-to-be-done**. The core objective is to simulate how different types of users interact with documents by highlighting the content that matters most to them.

---

## 📥 Input Specifications

- **Documents**: 3–10 related PDFs from any domain.
- **Persona**: Description of the role with domain knowledge (e.g., student, analyst, journalist).
- **Job-To-Be-Done**: Task the persona needs to accomplish using the given documents.

### 🧾 Example Scenarios

| Test Case | Persona | Documents | Job |
|----------|---------|-----------|-----|
| 1 | PhD Researcher in Computational Biology | 4 research papers on "Graph Neural Networks for Drug Discovery" | Prepare a literature review on methodologies, datasets, and benchmarks |
| 2 | Investment Analyst | 3 annual reports from tech companies (2022-2024) | Analyze revenue trends, R&D spend, market strategy |
| 3 | Chemistry Undergraduate | 5 chapters from organic chemistry textbooks | Summarize key concepts & mechanisms for exams |

---

## ✅ Output Structure (JSON)

A valid output consists of:
1. **Metadata**:
   - Input Documents
   - Persona
   - Job-to-be-done
   - Timestamp of processing

2. **Extracted Section**:
   - Document name
   - Page number
   - Section title
   - Importance rank (1 = highest)

3. **Sub-section Analysis**:
   - Document name
   - Refined Text (cleaned, concise content)
   - Page Number

Refer to the provided sample: `challenge1b_output.json`

---

## ⚙️ Technical Constraints

- Runs on **CPU only**
- Model size must be **≤ 1GB**
- Processing time must be **≤ 60 seconds** (for 3–5 docs)
- **No internet access** during execution

---

## 📂 Project Structure

```

round1b/
├── docs/                        # PDF documents for testing
├── src/
│   ├── extractor.py             # Core logic for section and sub-section extraction
│   ├── ranker.py                # Ranking based on persona-job match
│   ├── summarizer.py           # Sub-section refinement logic
│   └── utils.py                # Helper functions (PDF reading, text cleaning)
├── sample\_input/               # Sample PDFs, persona, job file
├── challenge1b\_output.json     # Expected output format
├── Dockerfile                  # Container configuration
├── approach\_explanation.md     # Methodology (300-500 words)
└── README.md                   # Project guide (this file)

````

---

## 🚀 Running the Project

### ✅ Prerequisites
- Docker installed (`v20+`)
- All input files are placed inside the `sample_input/` folder

### 📦 Build and Run

```bash
# Step 1: Build Docker image
docker build -t document-intelligence .

# Step 2: Run container
docker run --rm -v $(pwd)/sample_input:/app/sample_input document-intelligence
````

Output will be saved to `challenge1b_output.json`.

---

## 🧠 Methodology (Brief)

1. **Text Extraction**: PDFs are parsed and organized into per-page and per-section text blocks.
2. **Embedding and Matching**: The persona and job-to-be-done are converted into semantic embeddings using a compact NLP model. These are compared with section embeddings using cosine similarity.
3. **Ranking**: Sections and pages are ranked based on relevance score. Top-ranked sections are shortlisted.
4. **Sub-section Summarization**: Extracted content is cleaned and refined using a small transformer-based summarizer.
5. **Output Generation**: All results are written to JSON in the expected format.

For detailed explanation, see [`approach_explanation.md`](./approach_explanation.md)

---

## 🏆 Scoring Criteria Mapping

| Criterion             | Max Points | Approach Description                               |
| --------------------- | ---------- | -------------------------------------------------- |
| Section Relevance     | 60         | Context-aware similarity matching with persona/job |
| Sub-section Relevance | 40         | Cleaned, high-precision summary tailored to task   |

---
