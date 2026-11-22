# Precious Awuzu | Health data and service improvement

I work where healthcare operations, data analysis and customer service meet. In NHS occupational health, I investigate discrepancies in staff health records, prepare activity reports and support clients using OPAS G2. When callers kept asking how long referrals would take, I revised our letters to give them a realistic timeframe.

My MSc in Data Science (Merit) at the University of Gloucestershire focused on predicting hypertension. I also bring experience in residential care, resolving complex customer issues at Three UK, outbound business development and leading an administrative team in Nigeria.

[View the live portfolio](https://precious-awuzu.github.io/)

| Case study | Method and finding |
| --- | --- |
| [NHS referral demand by week, priority, specialty and commissioner](https://precious-awuzu.github.io/referrals.html) | I analysed 1,674,089 referrals recorded from 1 to 28 September 2025 across 62 specialties and 114 commissioner entries. Routine referrals made up 66.5% of demand overall and 85.2% in orthopaedics. The ten highest-volume commissioners accounted for 29.35% of all referrals. |
| [Predicting hypertension](https://precious-awuzu.github.io/research.html) | A decision tree and XGBoost both reached 99% reported accuracy in my MSc comparison. That tie leaves a clinical question open: how many positive cases did each model miss? |
| [Auditing AI-assisted support triage](https://precious-awuzu.github.io/governance.html) | At a threshold of 0.6, the example rules missed three of four urgent brief tickets and one of four urgent detailed tickets. Each subgroup contains only four positives, so one case shifts its miss rate by 25 percentage points. |
| [Investigating customer support handovers](https://precious-awuzu.github.io/quality.html) | I grouped 15 synthetic cases by handover count and measured repeat contact within seven days. The sample illustrates an association. It cannot establish whether extra handovers caused customers to call again. |

## Reproduce the handover analysis

From the repository root, run the following command with Python 3. The script uses the standard library and the included synthetic CSV.

```sh
python3 analysis/analyse_handovers.py analysis/support-cases.csv
```

| Handovers | Repeat contacts within seven days | Rate |
| --- | ---: | ---: |
| 0 | 1 of 5 | 20% |
| 1 | 2 of 5 | 40% |
| 2 or more | 4 of 5 | 80% |

The dissertation workbook contains 219 distinct subjects across four hypertension categories. The AI triage and customer support demonstrations use synthetic examples alongside published UK evidence from DWP and Ofcom.

## Skills in practice

- **Data analysis and modelling.** Python, pandas, scikit-learn, SQL, Excel and Power BI. My projects include analysing NHS referral volumes and comparing six hypertension classifiers.
- **Healthcare operations and governance.** Cohort, OPAS G2, data quality checks, KPI reporting and audit support. I built a Microsoft Lists tracker so administrators and clinical PAs could review appointment changes in one place.
- **Customer and team operations.** Customer retention, technical troubleshooting, CRM records, prospecting and team coordination. At Three UK, I handled complex orders and coached colleagues on compliance.

[Email Precious](mailto:preciousawuzu@outlook.com) · [LinkedIn](https://uk.linkedin.com/in/precious-awuzu-581737a3)
