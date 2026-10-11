# Cahier des charges — AI Job Application Agent

## 1. Problématique

L'analyse d'offres d'emploi, la comparaison avec un CV et la préparation de candidatures sont des tâches répétitives. L'application vise à assister le candidat tout en lui laissant le contrôle des décisions finales.

## 2. Objectif

Créer une application Python utilisant un modèle de langage, un workflow explicite et, dans une phase ultérieure, un système RAG et un agent IA doté d'outils contrôlés.

## 3. Fonctionnalités prévues

### MVP — première version
- Recevoir le texte d'une offre d'emploi.
- Recevoir le texte d'un CV de démonstration.
- Extraire les exigences et compétences du poste.
- Comparer les exigences aux éléments présents dans le CV.
- Produire un rapport structuré.
- Signaler les éléments non documentés plutôt que les inventer.

### Version suivante
- Charger des documents PDF.
- Ajouter le RAG : découpage, embeddings et recherche de passages pertinents.
- Générer une proposition de lettre de motivation.
- Ajouter une interface Streamlit.
- Ajouter des tests unitaires et d'intégration.

### Version avancée
- Introduire un agent IA et des outils autorisés.
- Ajouter une API FastAPI si utile.
- Ajouter Docker et GitHub Actions.
- Déployer une démonstration avec des données fictives.

## 4. Utilisateurs visés

Les personnes qui souhaitent analyser une offre et préparer une candidature personnalisée. Le projet est aussi une démonstration technique destinée aux recruteurs en IA générative et en ingénierie logicielle.

## 5. Workflow fonctionnel

1. Entrées : CV et offre d'emploi.
2. Validation des entrées.
3. Extraction et nettoyage du texte.
4. Extraction structurée des exigences du poste.
5. Recherche des éléments pertinents dans le CV.
6. Comparaison critère par critère.
7. Génération d'un rapport et de recommandations.
8. Vérification humaine et export éventuel.

## 6. Résultats attendus

- Un rapport lisible et justifié.
- Les compétences démontrées par le CV.
- Les compétences partiellement démontrées.
- Les exigences qui ne sont pas documentées.
- Des recommandations d'amélioration.
- Une proposition de lettre de motivation, soumise à validation humaine.

## 7. Critères d'acceptation

- L'application gère les entrées manquantes ou invalides.
- Les résultats distinguent faits documentés et suggestions du modèle.
- Les tests passent localement et via l'intégration continue.
- Le README permet à une autre personne de lancer le projet.
- Aucun secret ni document personnel n'est versionné.
- Aucune candidature n'est envoyée automatiquement.

## 8. Limites et précautions

Le système peut se tromper. Il ne doit pas inventer des expériences ou qualifications, et ne doit pas présenter un score de correspondance comme une probabilité d'embauche. Les résultats doivent être vérifiés par l'utilisateur.
