# Precious Awuzu | Health data and service improvement

I work in NHS occupational health and hold an MSc in Data Science from the University of Gloucestershire. My dissertation compared six approaches to hypertension prediction. My service projects grew out of questions I encounter at work, including how to tell who owns the next step in a referral.

[View the live portfolio](https://precious-awuzu.github.io/preciousawuzu.github.io/)

| Case study | Method and finding |
| --- | --- |
| [Predicting hypertension](https://precious-awuzu.github.io/preciousawuzu.github.io/research.html) | A decision tree and XGBoost both reached 99% reported accuracy in my MSc comparison. That tie leaves a clinical question open: how many positive cases did each model miss? |
| [Tracking a referral through review](https://precious-awuzu.github.io/preciousawuzu.github.io/clinic.html) | Five dated events trace one fictional referral from receipt to booking. The event history distinguishes time awaiting clarification from time awaiting clinical review. |
| [Auditing AI-assisted support triage](https://precious-awuzu.github.io/preciousawuzu.github.io/governance.html) | At a threshold of 0.6, the example rules missed three of four urgent brief tickets and one of four urgent detailed tickets. Each subgroup contains only four positives, so one case shifts its miss rate by 25 percentage points. |
| [Investigating customer support handovers](https://precious-awuzu.github.io/preciousawuzu.github.io/quality.html) | I grouped 15 synthetic cases by handover count and measured repeat contact within seven days. The sample illustrates an association. It cannot establish whether extra handovers caused customers to call again. |

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
