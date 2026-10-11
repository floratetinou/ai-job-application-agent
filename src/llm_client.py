
import ollama


def analyze_job_offer(
    job_offer,
    cv_text,
    required_skills,
    matched_skills,
    missing_skills,
    score,
):
    """Analysiert eine Stellenanzeige mit einem lokalen Ollama-Modell."""

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "system",
                "content": (
                    "Du bist ein professioneller Karriereassistent. "
                    "Antworte immer auf Deutsch. "
                    "Erfinde keine Fähigkeiten oder Erfahrungen. "
                    "Die von Python ermittelten Ergebnisse sind die "
                    "verbindliche Grundlage für die Schlüsselwortanalyse. "
                    "Ordne eine als vorhanden erkannte Fähigkeit nicht "
                    "gleichzeitig als fehlend ein. "
                    "Unterscheide zwischen vorhandenen Schlüsselwörtern "
                    "und nachgewiesener praktischer Erfahrung. "
                    "Ein fehlendes Schlüsselwort bedeutet nicht automatisch, "
                    "dass eine Person die Fähigkeit nicht besitzt. "
                    "Nenne konkrete nächste Schritte und weise auf "
                    "Unsicherheiten hin."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Stellenanzeige:\n{job_offer}\n\n"
                    f"Lebenslauf:\n{cv_text}\n\n"
                    f"Von Python erkannte Anforderungen:\n"
                    f"{required_skills}\n\n"
                    f"Im Lebenslauf erkannte Fähigkeiten:\n"
                    f"{matched_skills}\n\n"
                    f"Nicht im Lebenslauf erkannte Anforderungen:\n"
                    f"{missing_skills}\n\n"
                    f"Von Python berechneter Skill-Match-Score: {score}%\n\n"
                    "Erstelle eine strukturierte Analyse mit folgenden "
                    "Abschnitten:\n"
                    "1. Passende Fähigkeiten\n"
                    "2. Nicht im Lebenslauf dokumentierte Anforderungen\n"
                    "3. Einschätzung der fachlichen Passung\n"
                    "4. Konkrete nächste Schritte\n\n"
                    "Verändere weder die Python-Ergebnisse noch den Score. "
                    "Erkläre, dass der Score auf Schlüsselwörtern basiert "
                    "und keine vollständige Eignungsbewertung darstellt."
                ),
            },
        ],
    )

    return response["message"]["content"]


if __name__ == "__main__":
    job_offer = (
        "Wir suchen einen AI Engineer mit Python, RAG und Docker."
    )
    cv_text = (
        "Erfahrung mit Python, Machine Learning und Git."
    )

    required_skills = ["Python", "RAG", "Docker"]
    matched_skills = ["Python"]
    missing_skills = ["RAG", "Docker"]
    score = 33

    result = analyze_job_offer(
        job_offer,
        cv_text,
        required_skills,
        matched_skills,
        missing_skills,
        score,
    )

    print("\n===== KI-ANALYSE =====\n")
    print(result)
