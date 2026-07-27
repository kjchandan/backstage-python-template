# ${{ values.repoName }}

## Overview

This repository was automatically created using the Backstage Scaffolder Template.

---

## Repository Information

| Property | Value |
|----------|-------|
| Repository | ${{ values.repoName }} |
| System | ${{ values.system }} |
| Group | ${{ values.group }} |
| Component | ${{ values.component }} |

---

## Project Structure

```text
.
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

## Getting Started

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Application

```bash
python scripts/app.py
```

---

## Created By

Backstage Scaffolder

---