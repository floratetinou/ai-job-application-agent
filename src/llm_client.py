

import os

import ollama
from openai import OpenAI


def analyze_job_offer(
    job_offer,
    cv_text,
    required_skills,
    matched_skills,
    missing_skills,
    score,
):
    """Analysiert eine Stellenanzeige mit einem lokalen oder gehosteten LLM."""

    system_prompt = (
        "Du bist ein professioneller Karriereassistent. "
        "Antworte immer auf Deutsch. "
        "Erfinde keine Fähigkeiten oder Erfahrungen. "
        "Die von Python ermittelten Ergebnisse sind die verbindliche "
        "Grundlage für die Schlüsselwortanalyse. "
        "Ordne eine als vorhanden erkannte Fähigkeit nicht gleichzeitig "
        "als fehlend ein. "
        "Unterscheide zwischen vorhandenen Schlüsselwörtern und "
        "nachgewiesener praktischer Erfahrung. "
        "Ein fehlendes Schlüsselwort bedeutet nicht automatisch, "
        "dass eine Person die Fähigkeit nicht besitzt. "
        "Nenne konkrete nächste Schritte und weise auf Unsicherheiten hin."
    )

    user_prompt = (
        f"Stellenanzeige:\n{job_offer}\n\n"
        f"Lebenslauf:\n{cv_text}\n\n"
        f"Von Python erkannte Anforderungen:\n{required_skills}\n\n"
        f"Im Lebenslauf erkannte Fähigkeiten:\n{matched_skills}\n\n"
        f"Nicht im Lebenslauf erkannte Anforderungen:\n{missing_skills}\n\n"
        f"Von Python berechneter Skill-Match-Score: {score}%\n\n"
        "Erstelle eine strukturierte Analyse mit folgenden Abschnitten:\n"
        "1. Passende Fähigkeiten\n"
        "2. Nicht im Lebenslauf dokumentierte Anforderungen\n"
        "3. Einschätzung der fachlichen Passung\n"
        "4. Konkrete nächste Schritte\n\n"
        "Verändere weder die Python-Ergebnisse noch den Score. "
        "Erkläre, dass der Score auf Schlüsselwörtern basiert und keine "
        "vollständige Eignungsbewertung darstellt."
    )

    provider = os.getenv("LLM_PROVIDER", "ollama").lower()

    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "Der API-Schlüssel fehlt. Bitte OPENAI_API_KEY konfigurieren."
            )

        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.choices[0].message.content or ""

    if provider == "ollama":
        response = ollama.chat(
            model=os.getenv("OLLAMA_MODEL", "qwen2.5:3b"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return response["message"]["content"]

    raise ValueError(
        "Ungültiger LLM_PROVIDER. Verwende 'ollama' oder 'openai'."
    )
