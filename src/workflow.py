


from pathlib import Path
from llm_client import analyze_job_offer
from cv_reader import extract_text_from_pdf
import re



def contains_skill(text, skill):
    """Prüft, ob eine Fähigkeit als eigenständiger Begriff vorkommt."""
    pattern = rf"(?<!\w){re.escape(skill)}(?!\w)"
    return re.search(pattern, text, re.IGNORECASE) is not None


def extract_skills(job_offer):
    """Erkennt bekannte Fähigkeiten in einer Stellenanzeige."""
    skills = [
        "Python", "SQL", "Docker", "Git",
        "RAG", "Machine Learning", "LangGraph", "FastAPI"
    ]

    return [
        skill for skill in skills
        if contains_skill(job_offer, skill)
    ]


def compare_skills(required_skills, cv_text):
    """Vergleicht die geforderten Fähigkeiten mit dem Lebenslauf."""
    matched_skills = [
        skill for skill in required_skills
        if contains_skill(cv_text, skill)
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in matched_skills
    ]

    return matched_skills, missing_skills



def calculate_match_score(required_skills, matched_skills):
    """Berechnet den Anteil der erkannten passenden Fähigkeiten."""
    if not required_skills:
        return 0

    return round(
        len(matched_skills) / len(required_skills) * 100
    )


def format_skills(skills):
    """Formatiert Fähigkeiten als Markdown-Liste."""
    if not skills:
        return "- Keine erkannt"

    return "\n".join(f"- {skill}" for skill in skills)


def get_recommendation(matched, missing):
    """Erstellt eine einfache Empfehlung."""
    if not missing:
        return "Gute Übereinstimmung mit den erkannten Anforderungen."

    return (
        f"{len(matched)} Fähigkeiten erkannt. "
        f"Prüfe die folgenden Anforderungen genauer: "
        f"{', '.join(missing)}."
    )


def generate_report(required, matched, missing, score, ai_analysis):
    """Erstellt einen Markdown-Bericht zur Bewerbungsanalyse."""

    report = f"""# Bewerbungsanalyse

## 1. Schlüsselwortanalyse

### Erkannte Anforderungen
{format_skills(required)}

### Vorhandene Fähigkeiten
{format_skills(matched)}

### Fehlende oder nicht erkannte Fähigkeiten
{format_skills(missing)}

## 2. Automatisch berechneter Skill-Match-Score

**Übereinstimmung der erkannten Fähigkeiten: {score}%**

*Hinweis: Der Score basiert auf einer automatischen
Schlüsselworterkennung. Er bewertet weder die tatsächliche
Kompetenztiefe noch die gesamte Eignung für die Stelle.*

## 3. Empfehlung

{get_recommendation(matched, missing)}

## 4. Analyse durch das lokale Sprachmodell

{ai_analysis}

---
*Automatisch erstellt. Bitte Ergebnisse vor einer Bewerbung überprüfen.*
"""

    output_dir = Path("reports")
    output_dir.mkdir(exist_ok=True)

    report_path = output_dir / "bewerbungsanalyse.md"
    report_path.write_text(report, encoding="utf-8")

    print(f"\nBericht gespeichert: {report_path}")


def run_workflow(job_offer, cv_text):
    """Führt die Bewerbungsanalyse mit Regeln und einem lokalen LLM aus."""

    print("1. Stellenanzeige analysieren...")
    required = extract_skills(job_offer)

    print("2. Fähigkeiten mit dem Lebenslauf vergleichen...")
    matched, missing = compare_skills(required, cv_text)

    print("3. Skill-Match-Score berechnen...")
    score = calculate_match_score(required, matched)
    print(f"Skill-Match-Score: {score}%")

    print("4. Lokales Sprachmodell analysiert das Profil...")
    ai_analysis = analyze_job_offer(
    job_offer,
    cv_text,
    required,
    matched,
    missing,
    score,
)

    print("\n===== KI-ANALYSE =====\n")
    print(ai_analysis)

    generate_report(
        required,
        matched,
        missing,
        score,
        ai_analysis
    )





if __name__ == "__main__":
    # Pfad zum Lebenslauf festlegen
    cv_path = "data/lebenslauf.pdf"

    print("=== AI Job Application Agent ===")
    print("Bitte füge die Stellenanzeige ein.")
    print("Gib END in einer neuen Zeile ein, wenn du fertig bist.")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    job_offer = "\n".join(lines).strip()

    if not job_offer:
        print("Fehler: Es wurde keine Stellenanzeige eingegeben.")
    else:
        try:
            # Lebenslauf aus der PDF-Datei auslesen
            cv_text = extract_text_from_pdf(cv_path)

            print("\nLebenslauf erfolgreich eingelesen.")
            print(f"Extrahierte Zeichen: {len(cv_text)}")
            print("\nDie Analyse wird gestartet...\n")

            # Stellenanzeige analysieren und Bericht erstellen
            run_workflow(job_offer, cv_text)

        except (FileNotFoundError, ValueError) as error:
            print(f"Fehler beim Lesen des Lebenslaufs: {error}")
