# Project Structure

Where everything goes.

---

## Folder Layout

```
FINAL_PROJECT/
├── data/
│   ├── raw/                     # Original datasets (DO NOT MODIFY)
│   │   ├── wages/               # Wage data 2006-2024 (14 CSV files)
│   │   ├── 33100878-eng/        # AI planned adoption Q3 2024
│   │   └── 33101004-eng/        # AI actual usage Q2 2025
│   │
│   ├── cleaned/                 # Cleaned data (optional)
│   │   └── ai_exposure_by_industry.csv
│   │
│   ├── merged/                  # Final merged dataset
│   │   └── master_dataset.csv
│   │
│   └── metadata/                # Logs and notes
│       └── merge_log.md
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb   # Data cleaning (done)
│   └── 02_analysis.ipynb        # Analysis (to do)
│
├── outputs/
│   ├── figures/                 # Plots and charts
│   └── tables/                  # Summary stats
│
├── report/
│   └── final_report.pdf         # Final deliverable
│
├── docs/                        # Internal docs
│   ├── git_workflow.md
│   ├── progress.md
│   ├── submission_requirements.md
│   ├── data_dictionary.md
│   ├── project_structure.md
│   └── quick_start.md
│
├── venv/                        # Virtual environment (gitignored)
├── README.md
└── requirements.txt
```

---

## What Goes Where

**Raw data** → `data/raw/` (never modify)
**Cleaned data** → `data/cleaned/` or `data/merged/`
**Plots** → `outputs/figures/`
**Tables** → `outputs/tables/`
**Notebooks** → `notebooks/`
**Report** → `report/`

---

## File Names

**Raw data:**

- `wages_2024.csv`, `wages_2023.csv`, etc.
- `ai_planned_q3_2024.csv`
- `ai_actual_q2_2025.csv`

**Cleaned data:**

- `master_dataset.csv` (main file to use)
- `ai_exposure_by_industry.csv`

**Outputs:**

- `wage_trends.png`
- `entry_level_analysis.png`
- `summary_stats.csv`

---

## What NOT to Commit to Git

- `venv/` (virtual environment)
- `data/raw/` (too big)
- `.ipynb_checkpoints/`
- `__pycache__/`

These are in `.gitignore`
