# The Impact of AI on Canadian Wages

**SC/MATH 1130 A - Introduction to Data Science**
York University | Fall 2025

---

## Group Members

- Mickey Byalsky
- Ethan Kwan
- Jungmin Park
- Ejikeme Nwosu
- OJ Adeyemi

---

## What We're Doing

Analyzing how AI adoption affects Canadian workers - looking at wages, entry-level jobs, and which occupations are most at risk.

### Research Questions

1. **Historical Wage Growth** - Did AI-heavy industries see different wage trends (2012-2024) compared to low-AI sectors?

2. **Entry-Level Impact** - Is AI making it harder to get entry-level jobs and lowering starting wages?

3. **Occupational Vulnerability** - Which jobs and regions will benefit from AI vs which ones are at risk?

---

## Datasets

**1. Canadian Wage Data (2006-2024)**
- Job Bank data with wages by occupation, province, region
- ~613k rows across 14 CSV files
- Files: `data/raw/wages/wages_YYYY.csv`

**2. AI Planned Adoption (Q3 2024)**
- Stats Canada survey on businesses planning to use AI
- Files: `data/raw/33100878-eng/`

**3. AI Actual Usage (Q2 2025)**
- Stats Canada survey on businesses actually using AI
- Files: `data/raw/33101004-eng/`

---

## Setup

### 1. Create virtual environment
```bash
# use python3 on Mac/Linux, python on Windows
python3 -m venv venv

# activate it
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 2. Install packages
```bash
pip install -r requirements.txt
```

### 3. Run notebooks

**IMPORTANT: Run data cleaning first!**

Start with [01_data_cleaning.ipynb](notebooks/01_data_cleaning.ipynb) to create the master dataset, then run [02_analysis.ipynb](notebooks/02_analysis.ipynb).

**Option A: Jupyter in browser**
```bash
jupyter notebook
# then open notebooks/01_data_cleaning.ipynb first
```

**Option B: VSCode with Jupyter extension**
- Open `01_data_cleaning.ipynb` and click "Run All" at the top
- Make sure you select the venv kernel
- After cleaning finishes, open `02_analysis.ipynb`

---

## Workflow

### Notebook 1: Data Cleaning
- Load all wage data (2006-2024)
- Convert annual wages to hourly (÷ 2080 hours/year)
- Clean AI adoption data
- Map job titles to industries using keywords
- Flag entry-level jobs (bottom 25% of wages)
- Merge everything into master dataset
- Output: `data/merged/master_dataset.csv`

### Notebook 2: Analysis
- Section 2.1: Wage growth trends
- Section 2.2: Entry-level job analysis
- Section 2.3: Vulnerability assessment
- Outputs: charts in `outputs/figures/`, tables in `outputs/tables/`

---

## Master Dataset Columns

After running `01_data_cleaning.ipynb`, you'll have these columns to analyze:

**Identifiers:**
- `NOC_CNP`: occupation code
- `NOC_Title_Standardized`: clean job title
- `Province`: province code (ON, BC, etc.)
- `Region`: economic region name
- `Reference_Period`: year (2006-2024)

**Wage data (all in $/hour):**
- `Low_Wage_Hourly`: 10th percentile wage
- `Median_Wage_Hourly`: median wage
- `High_Wage_Hourly`: 90th percentile wage
- `Average_Wage_Hourly`: mean wage
- `Quartile1_Wage_Hourly`: 25th percentile
- `Quartile3_Wage_Hourly`: 75th percentile

**Flags:**
- `missing_wage_flag`: 1 if all wage data is missing (privacy suppression)
- `is_entry_level`: 1 if wage is in bottom 25%

**AI exposure:**
- `Industry`: mapped industry category
- `AI_Exposure_Score`: % of businesses using AI in that industry
- `AI_Exposure_Category`: Low/Medium/High

**Use these for analysis:**
- Compare `Median_Wage_Hourly` trends over `Reference_Period`
- Group by `AI_Exposure_Category` to see high-AI vs low-AI industries
- Filter `is_entry_level == 1` to analyze entry-level jobs
- Group by `Province` for regional differences

---

## Limitations

- AI exposure is measured at industry level (not specific jobs)
- ~60-95% of wage data missing due to Stats Canada privacy rules
- Entry-level jobs identified by 25th percentile wage (simple approach)
- Job-to-industry mapping uses keyword matching (not perfect)
- No breakdowns by gender/race

---

## Team Collaboration

This project is on GitHub: https://github.com/ojadeyemi/MATH_1130_Final_Project

**For team members:** See [git_workflow.md](docs/git_workflow.md) for how to clone the repo and work on branches.

---

## More Info

**Check `docs/` folder for:**
- [git_workflow.md](docs/git_workflow.md) - how to clone and work on branches
- [progress.md](docs/progress.md) - current status and what's next
- [submission_requirements.md](docs/submission_requirements.md) - what we need to submit for full marks
- [data_dictionary.md](docs/data_dictionary.md) - all column definitions
- [project_structure.md](docs/project_structure.md) - folder organization
- [quick_start.md](docs/quick_start.md) - fast setup guide
