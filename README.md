# AI Job Application Agent

Un projet de portfolio pour développer un agent IA qui analyse une offre d'emploi, la compare à un CV et prépare des recommandations de candidature.

## Objectif

Construire progressivement une application démontrant des compétences en :
- Python
- LLM et IA générative
- RAG (Retrieval-Augmented Generation)
- Agents IA et workflows
- Tests automatisés
- Git/GitHub, Docker et CI/CD

## Fonctionnement visé

1. Recevoir un CV et une offre d'emploi.
2. Extraire et nettoyer le texte.
3. Identifier les exigences du poste.
4. Rechercher les passages pertinents du CV.
5. Comparer les exigences avec les compétences documentées.
6. Générer un rapport structuré et des recommandations.
7. Proposer une lettre de motivation que l'utilisateur peut vérifier et modifier.

> L'application ne doit pas envoyer de candidature sans validation humaine. Un score éventuel doit être explicable et ne représente pas une probabilité de recrutement.

## État actuel

**Version 0 — Documentation et préparation.** Le code applicatif sera développé ensemble, étape par étape.

## Démarrage

Aucune dépendance n'est nécessaire pour lire la documentation.

Quand nous commencerons à coder, nous créerons un environnement virtuel Python et ajouterons les dépendances nécessaires.

## Structure du dépôt

```text
ai-job-application-agent/
├── README.md
├── PROJECT_PLAN.md
├── ARCHITECTURE.md
├── ROADMAP.md
├── .gitignore
├── .env.example
├── requirements.txt
├── src/
│   └── __init__.py
├── tests/
│   └── .gitkeep
├── data/
│   └── sample/
│       └── README.md
├── docs/
│   └── GLOSSARY.md
└── .github/
    └── workflows/
        └── tests.yml
```

## Confidentialité et sécurité

- Ne jamais publier de CV personnel ni de données personnelles dans le dépôt public.
- Ne jamais ajouter de clé API à GitHub.
- Utiliser `.env` pour les secrets locaux ; ce fichier doit rester ignoré par Git.
- Utiliser uniquement des exemples fictifs ou anonymisés dans le dossier `data/sample/`.

## Prochaines étapes

1. Créer un dépôt GitHub public ou privé.
2. Installer/configurer Python et un environnement virtuel.
3. Développer une première version simple du workflow.
4. Ajouter les tests, puis le RAG et les capacités d'agent.
5. Conteneuriser et déployer lorsque l'application fonctionne localement.
