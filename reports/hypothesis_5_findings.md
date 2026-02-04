# Hypothesis 5 — Model Uncertainty Reflects Prediction Reliability

## Hypothesis
Model uncertainty measures (prediction entropy and confidence margin) can be used to identify unreliable predictions, particularly in challenging tumor cases.

---

## Experimental Setup
A logistic regression model was trained using core morphological features
(`concavity_mean`, `perimeter_mean`, `radius_mean`, `area_mean`).  
For each test sample, uncertainty was quantified using:

- **Prediction entropy**
- **Confidence margin** (|p − 0.5|)
- Prediction error indicator (correct vs incorrect)

Uncertainty metrics were further analyzed across tumor size groups (Small, Medium, Large).

---

## Results

### Uncertainty by Tumor Size
| Tumor Size | Mean Entropy | Mean Confidence Margin |
|-----------|-------------|-----------------------|
| Small     | 0.17        | 0.46                  |
| Medium   | 0.43        | 0.32                  |
| Large    | 0.22        | 0.40                  |

Medium-sized tumors exhibited the **highest uncertainty**, reflected by both elevated entropy and reduced confidence margin.

---

### Error vs Uncertainty Relationship
Incorrect predictions were strongly concentrated in regions of:
- **High entropy**
- **Low confidence margin**

Correct predictions clustered around:
- Low entropy
- High confidence margin

This confirms that uncertainty metrics meaningfully capture prediction reliability.

---

### Calibration Analysis
The calibration curve showed deviations from the ideal diagonal, particularly in the mid-probability range, indicating mild miscalibration where uncertainty is highest.

---

## Conclusion
Hypothesis 5 is **supported**.  
Model uncertainty metrics provide actionable signals for identifying unreliable predictions and potential failure cases, especially in intermediate tumor presentations.
