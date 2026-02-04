# Hypothesis 3 — Failure Analysis of Engineered Geometric Features

## Hypothesis

**H3:** The engineered Irregularity Index fails to reliably detect malignancy in specific tumor subpopulations, particularly medium-sized tumors with low-to-moderate perimeter variance.

This hypothesis focuses on identifying *where* and *why* the model fails rather than improving aggregate performance.

---

## Motivation

In clinical and high-stakes machine learning systems, understanding systematic failure modes is as important as achieving strong overall accuracy. A feature that performs well globally may still be unreliable for certain subgroups, leading to undetected high-risk cases.

This hypothesis investigates whether the Irregularity Index exhibits such localized weaknesses.

---

## Experimental Setup

- A logistic regression model was trained using base geometric features and the engineered Irregularity Index.
- Predictions were analyzed at the sample level to identify false negatives (missed malignant cases).
- Tumors were bucketed into **Small**, **Medium**, and **Large** size groups based on perimeter statistics.
- Failure rates were computed per size bucket.
- A shallow decision tree (max depth = 3) was trained to expose rule-based failure regions.

---

## Results

### Failure Rate by Tumor Size

- **Small tumors:** No malignant cases detected as false negatives.
- **Medium tumors:** High false negative rate (~66%).
- **Large tumors:** Very low false negative rate (~2%).

This demonstrates a pronounced collapse in detection performance for **medium-sized tumors**, despite strong global metrics.

---

### Irregularity Index Distribution

Analysis of the Irregularity Index values showed substantial overlap between correctly detected and missed malignant cases within the medium-size bucket. The index does not sufficiently separate malignant and benign tumors in this region of the feature space.

---

### Decision Tree Analysis

The decision tree visualization revealed:

- **Perimeter mean** as the dominant root split.
- **Concavity mean** as the primary secondary discriminator.
- Medium-sized tumors with moderate concavity frequently fall into benign-predicted branches, explaining the observed false negatives.

The Irregularity Index does not appear as a primary decision boundary, indicating redundancy once raw geometric features are considered.

---

## Interpretation

Although the Irregularity Index is intuitively meaningful, it fails to capture subtle morphological differences in tumors that do not exhibit extreme size or concavity. Medium-sized tumors often represent a morphological gray zone where benign and malignant features overlap, reducing the effectiveness of derived geometric ratios.

This failure is not random but structurally induced by feature overlap and model decision boundaries.

---

## Conclusion

**Hypothesis 3 is supported.**

The Irregularity Index demonstrates a clear failure mode in medium-sized tumors, leading to a disproportionately high rate of missed malignancies. While the feature contributes to global discrimination, it is unreliable as a standalone or primary signal in this clinically critical subgroup.

---

## Implications

- Feature engineering must be evaluated under subgroup and failure-based analysis, not solely aggregate metrics.
- Interpretability tools such as decision trees are essential for uncovering hidden weaknesses in engineered features.
- Clinical deployment should incorporate additional diagnostic checks for medium-sized tumors rather than relying on geometric features alone.

---
## Clinical Interpretation

From a clinical perspective, the observed failure modes are significant. Medium-sized tumors with moderate boundary irregularity are more likely to be misclassified as benign, despite being malignant. These cases represent a diagnostic gray zone where morphological features overlap between benign and malignant presentations.

In clinical practice, such cases often warrant additional imaging, biopsy, or longitudinal monitoring rather than reliance on automated classification alone. The decision tree visualization highlights specific geometric thresholds at which model confidence shifts, offering clinicians transparent criteria for identifying high-risk cases.

These findings underscore the importance of combining probabilistic models with interpretable rule-based explanations when deploying machine learning systems in medical decision support.


## Limitations

- Tumor size buckets were defined using simple perimeter-based thresholds.
- The analysis is limited to a single dataset and imaging-derived features.
- More granular morphological or texture-based features may be required to resolve medium-size ambiguity.

---

## Future Work

- Incorporate texture and intensity-based features to improve discrimination in medium-sized tumors.
- Explore ensemble strategies that combine probabilistic and rule-based models.
- Validate findings across additional breast cancer imaging datasets.

