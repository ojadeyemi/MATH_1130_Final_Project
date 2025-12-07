# Git Workflow

How to clone and work on the project without conflicts.

**Repo:** https://github.com/ojadeyemi/MATH_1130_Final_Project

---

## First Time Setup

```bash
# clone repo
git clone https://github.com/ojadeyemi/MATH_1130_Final_Project.git
cd MATH_1130_Final_Project

# create virtual environment
python3 -m venv venv        # Mac/Linux
python -m venv venv         # Windows

# activate
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

# install packages
pip install -r requirements.txt
```

---

## Daily Workflow

### 1. Pull latest changes

```bash
git pull origin main
```

### 2. Create your branch

```bash
git checkout -b yourname-feature
# example: git checkout -b oj-analysis
```

### 3. Do your work

- Open Jupyter
- Edit notebooks
- Save outputs

### 4. Commit and push

```bash
git add .
git commit -m "what you did"
git push origin yourname-feature
```

### 5. Merge to main (when ready)

```bash
git checkout main
git pull origin main
git merge yourname-feature
git push origin main
```

---

## Common Commands

```bash
git status              # see what changed
git diff                # see exact changes
git branch              # list branches
git checkout main       # switch to main branch
git pull origin main    # get latest from GitHub
```

---

## Tips

- Always `git pull` before starting work
- Work on your own branch, not `main`
- Commit often with clear messages
- Push regularly so team can see progress
- Ask team before merging to main
