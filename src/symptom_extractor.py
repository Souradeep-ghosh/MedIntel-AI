import re

def symptoms_extract(text: str) -> list[str]:
    symptoms = re.findall(r'\b(?:fever|cough|headache|fatigue|nausea|vomiting|diarrhea|shortness of breath|chest pain|sore throat)\b', text.lower())
    return list(set(symptoms))


text = "The patient reported experiencing fever, cough, and fatigue. Additionally, they mentioned nausea and vomiting."

extracted_symptoms = symptoms_extract(text)
print(extracted_symptoms)