# Precious Awuzu | Health data and service improvement

I work in NHS occupational health and hold an MSc in Data Science (Merit). This portfolio brings together the service problems I have worked on and the analyses behind my technical work.

[Read about the referral letters, shared appointment tracker and record correction](https://precious-awuzu.github.io/#nhs-work)

[View the live portfolio](https://precious-awuzu.github.io/)

| Case study | Method and finding |
| --- | --- |
| [NHS referral demand by week, priority, specialty and commissioner](https://precious-awuzu.github.io/referrals.html) | I analysed 1,674,089 referrals recorded from 1 to 28 September 2025 across 62 specialties and 114 commissioner entries. Routine referrals made up 66.5% of demand overall and 85.2% in orthopaedics. The ten highest-volume commissioners accounted for 29.35% of all referrals. |
| [Classifying hypertension with stacked ensembles](https://precious-awuzu.github.io/research.html) | I tested whether combining six machine learning and deep learning models improved classification across four hypertension categories in a workbook of 219 subjects. The study compares two ensemble approaches before and after tuning. |
| [Auditing AI-assisted support triage](https://precious-awuzu.github.io/governance.html) | At a threshold of 0.6, the example rules missed three of four urgent brief tickets and one of four urgent detailed tickets. Each subgroup contains only four positives, so one case shifts its miss rate by 25 percentage points. |
| [Investigating customer support handovers](https://precious-awuzu.github.io/quality.html) | I grouped 15 synthetic cases by handover count and measured repeat contact within seven days. The sample illustrates an association. It cannot establish whether extra handovers caused customers to call again. |
| [Customer support tickets in R](https://precious-awuzu.github.io/tickets.html) | I reviewed 8,469 tickets across four channels. Email and phone volumes differed by just 11 tickets. |
| [US healthcare breach reporting and third-party risk](https://precious-awuzu.github.io/breaches.html) | I examined 692 US healthcare breach filings. Hacking or IT incidents accounted for 639 of them. |

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

The AI triage and customer support demonstrations use synthetic examples alongside published UK evidence from DWP and Ofcom.

## Skills and tools

- **Analysis.** Python, R, pandas, scikit-learn, SQL, Excel and Power BI.
- **Health information.** Cohort, OPAS G2, data quality checks, KPI reporting and audit support.
- **Customer and team operations.** Technical troubleshooting, customer retention, outbound prospecting and team coordination.

[Email Precious](mailto:preciousawuzu@outlook.com) · [LinkedIn](https://uk.linkedin.com/in/precious-awuzu-581737a3)

[GitHub profile](https://github.com/Precious-Awuzu)
