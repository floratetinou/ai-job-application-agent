# Architecture prévisionnelle

## Vue d'ensemble

```text
CV + offre d'emploi
        |
        v
Validation des entrées
        |
        v
Extraction et nettoyage du texte
        |
        v
Analyse des exigences de l'offre
        |
        v
Recherche dans le CV (RAG, phase ultérieure)
        |
        v
Comparaison critère par critère
        |
        v
Génération du rapport
        |
        v
Vérification humaine
```

## Composants envisagés

- **Interface** : Streamlit pour une démonstration simple.
- **Workflow** : Python au début ; LangGraph pourra être étudié ensuite.
- **LLM** : modèle accessible via une API ou un modèle local.
- **RAG** : embeddings et index vectoriel (FAISS ou Chroma, à choisir).
- **Tests** : pytest.
- **CI** : GitHub Actions.
- **Conteneurisation** : Docker.

## Principe de conception

Commencer par un workflow déterministe et facile à tester. Ajouter ensuite les capacités d'agent là où elles apportent une vraie valeur. Le modèle ne doit pas être autorisé à exécuter des actions externes non validées.
