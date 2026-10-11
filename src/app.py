
import streamlit as st
import tempfile
from pathlib import Path

from cv_reader import extract_text_from_pdf
from workflow import (
    extract_skills,
    compare_skills,
    calculate_match_score,
)
from llm_client import analyze_job_offer


st.set_page_config(
    page_title="AI Job Application Agent",
    page_icon="💼",
    layout="wide",
)

st.title("💼 AI Job Application Agent")
st.subheader("KI-gestützte Bewerbungsanalyse")

st.write(
    "Analysiere, wie gut dein Lebenslauf zu einer Stellenanzeige passt."
)

cv_file = st.file_uploader(
    "Lebenslauf als PDF hochladen",
    type=["pdf"],
)

job_offer = st.text_area(
    "Stellenanzeige einfügen",
    height=250,
    placeholder="Füge hier die vollständige Stellenanzeige ein...",
)

if st.button("Analyse starten", type="primary"):
    if cv_file is None:
        st.warning("Bitte lade zuerst deinen Lebenslauf als PDF hoch.")
    elif not job_offer.strip():
        st.warning("Bitte füge zuerst eine Stellenanzeige ein.")
    else:
        try:
            with st.spinner("Lebenslauf wird analysiert..."):
                with tempfile.NamedTemporaryFile(suffix=".pdf",
                    delete=False,
                ) as temp_file:
                    temp_file.write(cv_file.getvalue())
                    temp_path = Path(temp_file.name)

                try:
                    cv_text = extract_text_from_pdf(str(temp_path))
                finally:
                    temp_path.unlink(missing_ok=True)

            with st.spinner("Kompetenzen werden verglichen..."):
                required = extract_skills(job_offer)
                matched, missing = compare_skills(required, cv_text)
                score = calculate_match_score(required, matched)

            st.metric("Skill-Match-Score", f"{score}%")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### Erkannte Anforderungen")
                if required:
                    for skill in required:
                        st.write(f"- {skill}")
                else:
                    st.write("Keine bekannten Anforderungen erkannt.")

                st.markdown("### Vorhandene Fähigkeiten")
                if matched:
                    for skill in matched:
                        st.write(f"- {skill}")
                else:
                    st.write("Keine passenden Schlüsselwörter erkannt.")

            with col2:
                st.markdown("### Nicht erkannte Fähigkeiten")
                if missing:
                    for skill in missing:
                        st.write(f"- {skill}")
                else:
                    st.write("Keine fehlenden Schlüsselwörter erkannt.")

            with st.spinner("Lokales Sprachmodell analysiert das Profil..."):
                ai_analysis = analyze_job_offer(
                    job_offer,
                    cv_text,
                    required,
                    matched,
                    missing,
                    score,
                )

            st.markdown("## KI-Analyse")
            st.markdown(ai_analysis)

            st.caption(
                "Hinweis: Der Score basiert auf Schlüsselwörtern "
                "und ist keine vollständige Eignungsbewertung."
            )

        except Exception as error:
            st.error(
                f"Bei der Analyse ist ein Fehler aufgetreten: {error}"
            )
