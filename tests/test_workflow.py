
from src.workflow import extract_skills, compare_skills


def test_extract_skills():
    """Prüft, ob Fähigkeiten aus einer Stellenanzeige erkannt werden."""
    job_offer = "We need Python, Docker and RAG experience."

    result = extract_skills(job_offer)

    assert result == ["Python", "Docker", "RAG"]


def test_compare_skills():
    """Prüft den Abgleich zwischen Anforderungen und Lebenslauf."""
    required = ["Python", "SQL", "Docker"]
    cv_text = "Experience with Python and Docker."

    matched, missing = compare_skills(required, cv_text)

    assert matched == ["Python", "Docker"]
    assert missing == ["SQL"]
