# Quick Start

Fast setup guide.

---

## First Time Setup

### 1. Get the code

```bash
git clone https://github.com/ojadeyemi/MATH_1130_Final_Project.git
cd MATH_1130_Final_Project
```

### 2. Create virtual environment

```bash
python3 -m venv venv        # Mac/Linux
python -m venv venv         # Windows

source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
```

### 3. Install packages

```bash
pip install -r requirements.txt
```

---

## Running Notebooks

### Start Jupyter

```bash
source venv/bin/activate    # activate first
jupyter notebook
```

### Order to run:

1. `01_data_cleaning.ipynb` - creates master_dataset.csv
2. `02_analysis.ipynb` - analyzes the data

---

## Common Issues

**Can't find modules:**

```bash
source venv/bin/activate
pip install -r requirements.txt
```

**Encoding errors:**

- Wage files use `encoding='latin-1'`
- AI files use `encoding='utf-8'`

**Jupyter kernel not found:**

```bash
pip install ipykernel
python -m ipykernel install --user --name=venv
```

---

## Jupyter Shortcuts

- `Shift + Enter` - run cell
- `A` - insert cell above
- `B` - insert cell below
- `DD` - delete cell
- `M` - markdown mode
- `Y` - code mode

---

## Before Submitting

- [ ] Both notebooks run error-free top-to-bottom
- [ ] Figures saved to `outputs/figures/`
- [ ] Tables saved to `outputs/tables/`
- [ ] Final report in `report/`
- [ ] All files committed to Git
