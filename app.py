from fastapi import FastAPI
from pydantic import BaseModel
from src.symptom_extractor import symptoms_extract
from src.Preliminary_diagnosis import prel_diagnosis
from src.PubMed_NCBI_Articles import fetching_pubmed_articles_with_metadata
from src.Summarize_Article import summarize_text

app = FastAPI()

class SymptomInput(BaseModel):
    description: str

@app.post("/diagnosis")
def diagnosis(data: SymptomInput):
    symptom = symptoms_extract(data.description)
    diagnosis_result = prel_diagnosis(symptom)

    pubmed_article = fetching_pubmed_articles_with_metadata(" ".join(symptom))
    abstracts = " ".join(article["abstract"] for article in pubmed_article)
    summary = summarize_text(abstracts[:3000])

    return {
        "symptom": symptom,
        "diagnosis": diagnosis_result,
        "pubmed_summary": summary
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)