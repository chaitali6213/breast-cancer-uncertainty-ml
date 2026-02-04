### # Hypothesis 1 — Feature Discriminatory Power

## Hypothesis
The engineered Irregularity Index provides statistically significant discriminatory power beyond raw geometric features such as concavity and perimeter.

## Experimental Setup
Multiple logistic regression models were trained using controlled feature sets, including concavity-only and a full geometric feature set augmented with the Irregularity Index. Models were evaluated using ROC-AUC on a stratified 70/30 holdout set, with statistical comparison performed using the DeLong test.

## Results
While the combined model occasionally achieved slightly higher ROC-AUC values than the concavity-only model, the magnitude of improvement was small (~0.005 AUC) and inconsistent across train–test splits.

The DeLong test was selected to account for correlation between ROC curves evaluated on the same test set.

## Interpretation
The Irregularity Index does not provide reliable incremental discriminatory power beyond existing geometric features. Although intuitively appealing, its contribution appears redundant once raw concavity and size-related features are present.

## Conclusion
Hypothesis 1 is rejected based on lack of statistically significant improvement and observed instability across splits.

## Implications
This result highlights the importance of statistical validation in feature engineering. Intuitive or visually motivated features may not translate into meaningful performance gains once existing strong signals are accounted for.

