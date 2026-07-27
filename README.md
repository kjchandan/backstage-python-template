# Backstage Python Repository Template

## Overview

This repository contains a Backstage Scaffolder Template used to create Python repositories automatically in GitHub.

The template performs the following tasks:

- Creates a new GitHub repository
- Creates a README.md
- Creates a catalog-info.yaml
- Creates requirements.txt
- Creates requirements-dev.txt
- Creates a sample Python application
- Creates a GitHub Actions deployment workflow
- Registers the repository in Backstage Catalog

---

## User Inputs

The template asks the user for:

- System
- Group
- GitHub Organization
- Component
- Repository Name

All fields are mandatory.

---

## Generated Repository Structure

```
Repository

├── README.md
├── catalog-info.yaml
├── requirements.txt
├── requirements-dev.txt
├── scripts
│   └── app.py
└── .github
    └── workflows
        └── deployment.yml
```

---

## Technologies

- Backstage Scaffolder
- GitHub
- GitHub Actions
- Python
- YAML

---

## Repository Structure

```
backstage-python-template

├── template.yaml
├── README.md
├── docs
├── skeleton
```