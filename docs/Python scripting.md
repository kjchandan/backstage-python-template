# Python Scripting Guide

## Overview

This repository is generated automatically using the Backstage Scaffolder Template.

It contains a basic Python project structure with:

- README.md
- catalog-info.yaml
- requirements.txt
- requirements-dev.txt
- Sample Python application
- GitHub Actions workflow

---

# Folder Structure

```text
Repository

├── README.md
├── catalog-info.yaml
├── requirements.txt
├── requirements-dev.txt
├── scripts
│     └── app.py
└── .github
      └── workflows
            └── deployment.yml
```

---

# Python Version

Python 3.12

---

# Create Virtual Environment

Windows

```bash
python -m venv venv
```

Linux / Mac

```bash
python3 -m venv venv
```

---

# Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

Development dependencies

```bash
pip install -r requirements-dev.txt
```

---

# Run Application

```bash
python scripts/app.py
```

Application URL

```
http://localhost:5000
```

Health Check

```
http://localhost:5000/health
```

---

# Run Tests

```bash
pytest
```

---

# Code Formatting

```bash
black .
```

---

# Static Code Analysis

```bash
flake8 .
```

---

# Test Coverage

```bash
coverage run -m pytest
coverage report
```

---

# GitHub Actions

Whenever code is pushed to the main branch:

- Repository is checked out
- Python is installed
- Dependencies are installed
- Python syntax is verified
- Unit tests are executed

---

# Backstage

This project is created using a Backstage Scaffolder Template.

The following values are supplied automatically by Backstage during project creation:

- Repository Name
- System
- Group
- Component
- GitHub Organization

---

# Maintainer

Platform Engineering Team