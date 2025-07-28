import fitz  # PyMuPDF
import spacy
import os
import json

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_entities_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    results = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        if not text.strip():
            continue

        spacy_doc = nlp(text)
        for ent in spacy_doc.ents:
            results.append({
                "text": ent.text,
                "label": ent.label_,
                "page": page_num + 1
            })

    return results

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"

    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, file)
            entities = extract_entities_from_pdf(pdf_path)

            output_path = os.path.join(output_dir, file.replace(".pdf", "_entities.json"))
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(entities, f, indent=2)

if __name__ == "__main__":
    main()
