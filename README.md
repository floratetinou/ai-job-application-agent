# AI Job Application Agent

An AI-powered job application assistant that analyzes job descriptions, compares role requirements with a candidate's documented skills and experience, and generates actionable recommendations to improve job applications.

This project is being developed as a hands-on portfolio project to demonstrate practical skills in Python, Large Language Models (LLMs), Generative AI, Retrieval-Augmented Generation (RAG), workflow orchestration, and software engineering.

## Project Objectives

The goal is to build a modular, maintainable, and testable AI application that combines traditional Python logic with LLM-powered analysis.

Key areas of focus:

- **Python Development** — modular architecture, clean code, and reusable components.
- **LLMs & Generative AI** — local language models and structured text generation.
- **Retrieval-Augmented Generation (RAG)** — retrieving relevant information from candidate documents to ground AI-generated responses.
- **AI Workflows & Agents** — orchestrating processing steps and integrating LLM capabilities into a controlled workflow.
- **Automated Testing** — validating core functionality with `pytest`.
- **API & Application Development** — exposing functionality through a user-friendly interface and, potentially, a REST API.
- **DevOps & CI/CD** — Git, GitHub Actions, Docker, and automated quality checks.

## Planned Features

The application is intended to support the following workflow:

1. **Input Processing** — accept a CV and a job description.
2. **Text Extraction** — extract and normalize text from the provided documents.
3. **Requirement Identification** — identify relevant skills, qualifications, and experience requirements.
4. **Document Retrieval** — retrieve relevant passages from the candidate's documents using RAG.
5. **Skills & Experience Analysis** — compare job requirements with documented qualifications and identify potential gaps.
6. **LLM-Powered Evaluation** — interpret relevant experience, identify transferable skills, and explain the analysis.
7. **Report Generation** — produce a structured report with findings and actionable recommendations.
8. **Cover Letter Assistance** — generate a draft cover letter for the candidate to review and edit.

## Technical Architecture

The application will combine deterministic Python processing with LLM-based reasoning.

| Component | Responsibility |
|---|---|
| Python workflow | Orchestrates the application steps |
| Python processing modules | Extract text, identify keywords, and apply deterministic rules |
| Local LLM via Ollama | Interpret job requirements and generate contextual recommendations |
| RAG pipeline | Retrieve relevant information from candidate documents |
| Automated tests | Validate expected behavior and reduce regressions |
| Reporting module | Generate structured analysis reports |

The architecture will evolve incrementally as new capabilities are implemented and tested.

## Technology Stack

**Current technologies**
- Python
- Ollama
- `pytest`
- Git and GitHub

**Planned technologies**
- Retrieval-Augmented Generation (RAG)
- Embeddings and vector search
- LangGraph or another workflow orchestration framework
- Streamlit for the user interface
- FastAPI for a possible REST API
- Docker
- GitHub Actions for CI/CD

Technologies will be integrated progressively as the project develops.

## Project Status

**Current phase: Initial implementation**

The repository began as a documentation and project-planning scaffold. The first implementation now includes a basic Python workflow for keyword-based skill extraction and comparison, automated tests, Markdown report generation, and an initial Ollama integration for LLM-based analysis.

The next milestones are to validate the end-to-end workflow, improve error handling and test coverage, and progressively introduce document retrieval and RAG.

## Getting Started

### Prerequisites

- Python
- Git
- Ollama installed locally
- A compatible Ollama model downloaded before running the LLM component

### Setup

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/floratetinou/ai-job-application-agent.git
cd ai-job-application-agent
```

Create and activate a virtual environment on Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project dependencies:

```powershell
python -m pip install -r requirements.txt
```

If Ollama is installed, download the model used by the application:

```powershell
ollama pull qwen2.5:3b
```

Run the current workflow:

```powershell
python src\workflow.py
```

Run the automated tests:

```powershell
python -m pytest -v
```

**Note:** Setup commands may evolve as dependencies and project modules are finalized.

## Repository Structure

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
│   ├── __init__.py
│   ├── workflow.py
│   └── llm_client.py
├── tests/
│   └── test_workflow.py
├── data/
│   └── sample/
│       └── README.md
├── docs/
│   └── GLOSSARY.md
└── .github/
    └── workflows/
        └── tests.yml
```

The tree reflects the intended/current working structure; files may be added as development progresses.

## Privacy, Security & Responsible AI

- Never commit personal CVs, contact details, or other sensitive information to a public repository.
- Never commit API keys, passwords, or other secrets.
- Keep local environment files such as `.env` excluded from Git.
- Use fictional or anonymized documents for testing and demonstrations.
- Treat LLM-generated recommendations as suggestions, not objective assessments.
- Make analysis criteria and any compatibility score explainable.
- Do not interpret a compatibility score as a probability of being hired.
- Require explicit human review before any application is submitted.

## Roadmap

- [x] Create project documentation and repository structure
- [x] Implement initial keyword-based skill extraction and comparison
- [x] Add automated tests for core workflow functions
- [x] Generate a Markdown analysis report
- [x] Add initial local LLM integration with Ollama
- [ ] Validate and improve the end-to-end workflow
- [ ] Improve error handling and test coverage
- [ ] Add CV document upload and text extraction
- [ ] Implement document retrieval and RAG
- [ ] Improve structured output and recommendation quality
- [ ] Add a Streamlit interface
- [ ] Evaluate the benefits of a dedicated orchestration framework
- [ ] Add Docker support and CI/CD improvements
- [ ] Consider REST API integration and deployment

## Learning Goals

This project is designed to explore how conventional software engineering, deterministic processing, LLMs, and RAG can work together in a practical AI application.

The emphasis is on building a transparent and testable system rather than using an LLM for every operation.