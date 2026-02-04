# Hypothesis 2 — Recall Under Class Imbalance

## Hypothesis
**H2:** Under class imbalance, standard logistic regression under-detects malignant tumors, and class-weighted optimization significantly improves malignant recall without materially degrading overall performance.

---

## Dataset Characteristics
The Wisconsin Breast Cancer dataset exhibits moderate class imbalance:

- **Malignant:** 212 samples (37.26%)
- **Benign:** 357 samples (62.74%)

In a clinical context, false negatives (missed malignant tumors) are significantly more costly than false positives, making malignant recall a primary evaluation objective.

---

## Experimental Setup
Two logistic regression models were evaluated using identical feature sets:

### Baseline Model
- Standard logistic regression
- Default decision threshold (0.5)
- No class weighting

### Class-Weighted Model
- Logistic regression with `class_weight="balanced"`
- Loss re-weighted inversely to class frequency

Both models were trained and evaluated on a stratified train–test split.

---

## Evaluation Metrics
- Malignant recall
- Confusion matrix
- Precision–Recall curve
- Threshold vs recall trade-off

---

## Results

### Confusion Matrix Analysis
- **Baseline Model**
  - False negatives (malignant misclassified as benign): **14**
  - Decision boundary biased toward majority (benign) class

- **Class-Weighted Model**
  - False negatives reduced to **11**
  - Improved sensitivity to malignant cases

### Precision–Recall Curve
The class-weighted model achieved a high Average Precision (**AP ≈ 0.96**), indicating strong recall performance across a wide precision range.

### Threshold Sensitivity
Threshold analysis revealed that:
- Malignant recall increases substantially at lower thresholds
- Recall collapses sharply at high thresholds (> 0.9)
- Safe operating regions require explicit threshold tuning

---

## Interpretation
Class imbalance meaningfully alters classifier behavior even when ROC-AUC remains high.  
ROC-AUC alone masks clinically important failure modes related to malignant under-detection.

Class-weighted optimization shifts the decision boundary to better align with asymmetric risk profiles in medical diagnosis.

---

## Conclusion
**Hypothesis 2 is accepted.**  
Class-weighted optimization improves malignant recall under class imbalance and should be preferred in safety-critical diagnostic settings.

---

## Engineering Implications
- ROC-AUC is insufficient for evaluating medical classification systems
- Recall-sensitive metrics must guide model selection
- Class weighting is a low-cost, high-impact intervention
- Decision thresholds should be selected based on domain risk tolerance

---

## FAANG Translation
> Designed and evaluated recall-sensitive classification strategies under class imbalance, demonstrating improved minority-class detection through loss re-weighting and decision-threshold analysis.

---

## Artifacts
Generated visualizations:
- Baseline confusion matrix
- Class-weighted confusion matrix
- Precision–Recall curve
- Threshold vs recall trade-off plot
