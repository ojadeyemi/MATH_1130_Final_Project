#!/usr/bin/env python3
"""
Quick validation script to check project setup.
Run this to ensure all data files and folders are in place.
"""

from pathlib import Path
import sys

def check_directories():
    """Check if all required directories exist."""
    required_dirs = [
        'data/raw/wages',
        'data/raw/33100878-eng',
        'data/raw/33101004-eng',
        'data/cleaned',
        'data/merged',
        'data/metadata',
        'outputs/figures',
        'outputs/tables',
        'notebooks',
        'docs',
        'report'
    ]

    print("📁 Checking directories...")
    all_good = True
    for dir_path in required_dirs:
        path = Path(dir_path)
        if path.exists():
            print(f"  ✅ {dir_path}")
        else:
            print(f"  ❌ {dir_path} - MISSING")
            all_good = False

    return all_good

def check_data_files():
    """Check if raw data files exist."""
    print("\n📊 Checking raw data files...")

    # Check wage files (should have 2012-2025)
    wage_dir = Path('data/raw/wages')
    if wage_dir.exists():
        wage_files = list(wage_dir.glob('wages_*.csv'))
        print(f"  Wage files: {len(wage_files)}/14 found")
        if len(wage_files) < 14:
            print(f"    ⚠️  Expected 14 files (2012-2025), found {len(wage_files)}")
            return False
    else:
        print("  ❌ Wage directory not found")
        return False

    # Check AI planned adoption
    ai_planned = Path('data/raw/33100878-eng/ai_planned_q3_2024.csv')
    if ai_planned.exists():
        print(f"  ✅ AI Planned (Q3 2024)")
    else:
        print(f"  ❌ AI Planned (Q3 2024) - MISSING")
        return False

    # Check AI actual usage
    ai_actual = Path('data/raw/33101004-eng/ai_actual_q2_2025.csv')
    if ai_actual.exists():
        print(f"  ✅ AI Actual (Q2 2025)")
    else:
        print(f"  ❌ AI Actual (Q2 2025) - MISSING")
        return False

    return True

def check_notebooks():
    """Check if notebooks exist."""
    print("\n📓 Checking notebooks...")
    notebooks = [
        'notebooks/01_data_cleaning.ipynb',
        'notebooks/02_analysis.ipynb'
    ]

    all_good = True
    for nb in notebooks:
        path = Path(nb)
        if path.exists():
            print(f"  ✅ {nb}")
        else:
            print(f"  ❌ {nb} - MISSING")
            all_good = False

    return all_good

def check_docs():
    """Check if documentation files exist."""
    print("\n📚 Checking documentation...")
    docs = [
        'README.md',
        'requirements.txt',
        'docs/project_structure.md',
        'docs/task_assignments.md',
        'docs/data_dictionary.md',
        'docs/quick_start.md'
    ]

    all_good = True
    for doc in docs:
        path = Path(doc)
        if path.exists():
            print(f"  ✅ {doc}")
        else:
            print(f"  ❌ {doc} - MISSING")
            all_good = False

    return all_good

def main():
    print("=" * 60)
    print("🔍 FINAL_PROJECT Setup Validation")
    print("=" * 60)

    checks = [
        ("Directories", check_directories()),
        ("Data Files", check_data_files()),
        ("Notebooks", check_notebooks()),
        ("Documentation", check_docs())
    ]

    print("\n" + "=" * 60)
    print("📋 Summary")
    print("=" * 60)

    all_passed = True
    for name, passed in checks:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {name}: {status}")
        if not passed:
            all_passed = False

    print("=" * 60)

    if all_passed:
        print("\n🎉 All checks passed! You're ready to start working.")
        print("\nNext steps:")
        print("  1. Activate virtual environment: source venv/bin/activate")
        print("  2. Install dependencies: pip install -r requirements.txt")
        print("  3. Open Jupyter: jupyter notebook")
        print("  4. Start with: notebooks/01_data_cleaning.ipynb")
        return 0
    else:
        print("\n⚠️  Some checks failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("  - Missing data? Check docs/data_dictionary.md for download links")
        print("  - Missing directories? They should auto-create when running notebooks")
        return 1

if __name__ == "__main__":
    sys.exit(main())
