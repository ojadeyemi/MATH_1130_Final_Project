# Data Dictionary

Comprehensive guide to all columns in our datasets.

---

## Dataset 1: Canadian Wages (2006-2024)

**Source:** Employment and Social Development Canada (ESDC)
**Files:** `data/raw/wages/wages_YYYY.csv`

| Column Name                        | Type    | Description                               | Example Values                             |
| ---------------------------------- | ------- | ----------------------------------------- | ------------------------------------------ |
| `NOC_CNP`                          | String  | National Occupational Classification code | "NOC_00010", "NOC_21211"                   |
| `NOC_Title_eng`                    | String  | English occupation title                  | "Software developers", "Registered nurses" |
| `NOC_Title_fra`                    | String  | French occupation title                   | "Développeurs de logiciels"                |
| `prov`                             | String  | Province code                             | "ON", "QC", "NAT"                          |
| `ER_Code_Code_RE`                  | String  | Economic region code                      | "ER00", "ER3520"                           |
| `ER_Name`                          | String  | Economic region name (English)            | "Toronto", "Canada"                        |
| `Nom_RE`                           | String  | Economic region name (French)             | "Toronto", "Canada"                        |
| `Low_Wage_Salaire_Minium`          | Float   | Minimum wage (hourly or annual)           | 15.00, 31200                               |
| `Median_Wage_Salaire_Median`       | Float   | Median wage (hourly or annual)            | 25.00, 52000                               |
| `High_Wage_Salaire_Maximal`        | Float   | Maximum wage (hourly or annual)           | 45.00, 93600                               |
| `Average_Wage_Salaire_Moyen`       | Float   | Average wage (hourly or annual)           | 28.50, 59280                               |
| `Quartile1_Wage_Salaire_Quartile1` | Float   | 25th percentile wage                      | 18.00, 37440                               |
| `Quartile3_Wage_Salaire_Quartile3` | Float   | 75th percentile wage                      | 35.00, 72800                               |
| `Data_Source_E`                    | String  | Data source (English)                     | "2021 Census"                              |
| `Data_Source_F`                    | String  | Data source (French)                      | "Recensement 2021"                         |
| `Reference_Period`                 | Integer | Year of data                              | 2024, 2023, 2022                           |
| `Revision_Date_Date_revision`      | Date    | Last update date                          | "2024-12-03"                               |
| `Annual_Wage_Flag_Salaire_annuel`  | Integer | 0 = hourly, 1 = annual                    | 0, 1                                       |
| `Wage_Comment_E`                   | String  | Notes (English)                           | "Wages presented at annual rate..."        |
| `Wage_Comment_F`                   | String  | Notes (French)                            | "Pour cette profession..."                 |
| `Non_WageBen_pct`                  | Float   | Non-wage benefits percentage              | 62.8                                       |

### Missing Values

- Empty cells in wage columns indicate insufficient data for that region/occupation
- See `Wage_Comment_E` for explanations

---

## Dataset 2: AI Planned Adoption (Q3 2024)

**Source:** Statistics Canada Table 33-10-0878-01
**File:** `data/raw/33100878-eng/ai_planned_q3_2024.csv`

| Column Name                         | Type    | Description                               | Example Values                                                          |
| ----------------------------------- | ------- | ----------------------------------------- | ----------------------------------------------------------------------- |
| `REF_DATE`                          | Integer | Reference year                            | 2024                                                                    |
| `GEO`                               | String  | Geography                                 | "Canada"                                                                |
| `DGUID`                             | String  | Dissemination geography unique identifier | "2021A000011124"                                                        |
| `Business characteristics`          | String  | Industry or business attribute            | "Manufacturing", "1 to 4 employees"                                     |
| `Use of artificial intelligence...` | String  | AI adoption status (VERY LONG NAME)       | "Yes, business plans to use AI...", "Type of AI application planned..." |
| `UOM`                               | String  | Unit of measure                           | "Percent"                                                               |
| `UOM_ID`                            | Integer | Unit of measure ID                        | 239                                                                     |
| `SCALAR_FACTOR`                     | String  | Scaling factor                            | "units"                                                                 |
| `SCALAR_ID`                         | Integer | Scaling ID                                | 0                                                                       |
| `VECTOR`                            | String  | Vector identifier                         | "v1594336625"                                                           |
| `COORDINATE`                        | String  | Coordinate reference                      | "1.1.1"                                                                 |
| `VALUE`                             | Float   | Percentage value                          | 10.6, 18.8, 15.4                                                        |
| `STATUS`                            | String  | Data quality rating                       | "A", "B", "C", "D", "E", "F"                                            |
| `SYMBOL`                            | String  | Symbol                                    | (usually empty)                                                         |
| `TERMINATED`                        | String  | Termination flag                          | (usually empty)                                                         |
| `DECIMALS`                          | Integer | Decimal places                            | 1                                                                       |

### Status Symbols

- **A**: Excellent data quality
- **B**: Very good data quality
- **C**: Good data quality
- **D**: Acceptable data quality
- **E**: Use with caution
- **F**: Too unreliable to be published

---

## Dataset 3: AI Actual Usage (Q2 2025)

**Source:** Statistics Canada Table 33-10-1004-01
**File:** `data/raw/33101004-eng/ai_actual_q2_2025.csv`

| Column Name                         | Type    | Description                               | Example Values                                               |
| ----------------------------------- | ------- | ----------------------------------------- | ------------------------------------------------------------ |
| `REF_DATE`                          | Integer | Reference year                            | 2025                                                         |
| `GEO`                               | String  | Geography                                 | "Canada"                                                     |
| `DGUID`                             | String  | Dissemination geography unique identifier | "2021A000011124"                                             |
| `Business characteristics`          | String  | Industry or business attribute            | "Manufacturing", "5 to 19 employees"                         |
| `Use of artificial intelligence...` | String  | AI usage status (VERY LONG NAME)          | "Yes, business used AI...", "Type of AI application used..." |
| `UOM`                               | String  | Unit of measure                           | "Percent"                                                    |
| `UOM_ID`                            | Integer | Unit of measure ID                        | 239                                                          |
| `SCALAR_FACTOR`                     | String  | Scaling factor                            | "units"                                                      |
| `SCALAR_ID`                         | Integer | Scaling ID                                | 0                                                            |
| `VECTOR`                            | String  | Vector identifier                         | "v1671082146"                                                |
| `COORDINATE`                        | String  | Coordinate reference                      | "1.1.1"                                                      |
| `VALUE`                             | Float   | Percentage value                          | 12.2, 18.6, 23.1                                             |
| `STATUS`                            | String  | Data quality rating                       | "A", "B", "C", "D", "E", "F"                                 |
| `SYMBOL`                            | String  | Symbol                                    | (usually empty)                                              |
| `TERMINATED`                        | String  | Termination flag                          | (usually empty)                                              |
| `DECIMALS`                          | Integer | Decimal places                            | 1                                                            |

---

## Master Dataset (After Cleaning)

### master_dataset.csv

**Location:** `data/merged/master_dataset.csv`
**Created by:** 01_data_cleaning.ipynb

This is the main file to use for analysis. It has 613k rows and 17 columns.

**Columns:**

- `NOC_CNP` - occupation code
- `NOC_Title_Standardized` - clean job title (merged duplicates)
- `Province` - province code (ON, BC, etc.)
- `Region` - economic region name
- `Reference_Period` - year (2006-2024)
- `Annual_Wage_Flag_Salaire_annuel` - 0 = hourly, 1 = annual
- `Low_Wage_Hourly` - 10th percentile wage ($/hour)
- `Median_Wage_Hourly` - median wage ($/hour)
- `High_Wage_Hourly` - 90th percentile wage ($/hour)
- `Average_Wage_Hourly` - mean wage ($/hour)
- `Quartile1_Wage_Hourly` - 25th percentile ($/hour)
- `Quartile3_Wage_Hourly` - 75th percentile ($/hour)
- `missing_wage_flag` - 1 if all wages missing, 0 otherwise
- `is_entry_level` - 1 if wage in bottom 25%, 0 otherwise
- `Industry` - mapped industry category (keyword-based)
- `AI_Exposure_Score` - % businesses using AI in that industry
- `AI_Exposure_Category` - Low/Medium/High

### ai_exposure_by_industry.csv

**Location:** `data/cleaned/ai_exposure_by_industry.csv`

Lookup table showing AI exposure score for each industry (67 industries total).

---

## Common NAICS Industries

| NAICS Code | Industry Name                                   |
| ---------- | ----------------------------------------------- |
| 11         | Agriculture, forestry, fishing and hunting      |
| 21         | Mining, quarrying, and oil and gas extraction   |
| 23         | Construction                                    |
| 31-33      | Manufacturing                                   |
| 41         | Wholesale trade                                 |
| 44-45      | Retail trade                                    |
| 48-49      | Transportation and warehousing                  |
| 51         | Information and cultural industries             |
| 52         | Finance and insurance                           |
| 53         | Real estate and rental and leasing              |
| 54         | Professional, scientific and technical services |
| 56         | Administrative and support services             |
| 62         | Health care and social assistance               |
| 71         | Arts, entertainment and recreation              |
| 72         | Accommodation and food services                 |
| 81         | Other services                                  |

---

## Common NOC Categories

| NOC Code | Occupation Category                       |
| -------- | ----------------------------------------- |
| 0        | Management occupations                    |
| 1        | Business, finance and administration      |
| 2        | Natural and applied sciences              |
| 3        | Health occupations                        |
| 4        | Education, law and social services        |
| 5        | Art, culture, recreation and sport        |
| 6        | Sales and service                         |
| 7        | Trades, transport and equipment operators |
| 8        | Natural resources, agriculture            |
| 9        | Manufacturing and utilities               |
