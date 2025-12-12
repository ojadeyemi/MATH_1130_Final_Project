# Master Dataset Metadata
Generated: 2025-12-06 21:35:31.730038

## Summary
- Rows: 613,008
- Columns: 17
- Years: 2006.0 to 2024.0
- Provinces: 16
- NOC codes: 500
- Occupations: 515

## Sources
1. Job Bank wage data (2012-2024) - 613,008 rows
2. AI planned Q3 2024 - 938 rows  
3. AI actual Q2 2025 - 938 rows

## What we did
1. Converted annual wages to hourly (2080 hrs/year)
2. Flagged missing wage data
3. Standardized job titles
4. Merged similar titles (software engineer -> software developer)
5. Flagged entry level jobs (bottom 25% wages)
6. Mapped jobs to industries using keywords
7. Calculated AI exposure per industry
8. Merged wages with AI data
9. Created AI exposure categories

## Columns
- NOC_CNP: occupation code
- NOC_Title_Standardized: job title
- Province: province code
- Region: economic region
- Industry: mapped industry
- Reference_Period: year
- Low/Median/High/Average/Q1/Q3 Wage_Hourly: wage stats
- missing_wage_flag: 1 if all wages missing
- is_entry_level: 1 if bottom 25% wage
- AI_Exposure_Score: % businesses using AI
- AI_Exposure_Category: Low/Medium/High

## Notes
- 383,375 rows have no wage data
- NOC to industry mapping is approximate (keyword based)
- Entry level = wages <= 25th percentile for that occupation
