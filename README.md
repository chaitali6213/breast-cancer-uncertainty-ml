# Breast Cancer Risk Modeling with Uncertainty-Aware Decision Support

This project explores how traditional machine learning models for breast cancer classification can **fail silently**, especially under real-world clinical conditions such as class imbalance, small tumor size, and borderline feature values.

Rather than focusing only on accuracy, this work investigates **model behavior, failure modes, and uncertainty**, and proposes how **Agentic AI and Retrieval-Augmented Reasoning (RAAG)** can be used as a clinical decision-support layer.

---

##  Motivation

Most ML models for medical diagnosis are evaluated using aggregate metrics (accuracy, AUC).  
However, in clinical practice:

- False negatives are more dangerous than false positives  
- Small or early-stage tumors are harder to classify  
- Models may appear confident even when they are wrong  

This project asks a simple but critical question:

> *Can we trust a model’s prediction when it matters most?*

---

##  Dataset

- **Wisconsin Breast Cancer Dataset**
- Publicly available, structured clinical features
- Binary classification: Benign vs Malignant

---

##  Research Hypotheses

### **H1 — Feature Discriminatory Power**
Certain morphological features (e.g., concavity, perimeter) dominate predictions and may overshadow subtler signals.

### **H2 — Recall Under Class Imbalance**
Optimizing for accuracy leads to poor recall for malignant cases unless explicitly corrected.

### **H3 — Failure Mode Analysis**
Model failures are not random; they correlate with tumor size and feature overlap.

### **H4 — Small Tumor Feature Collapse**
For small tumors, benign and malignant feature distributions overlap significantly, reducing separability.

### **H5 — Model Uncertainty as a Risk Signal**
Higher prediction uncertainty (entropy, low confidence margin) aligns with higher error rates.

Each hypothesis is supported by experiments, visualizations, and written findings.

---

##  Key Results (High-Level)

- Recall for malignant cases improves with class-weighted models but introduces new uncertainty regions  
- Small tumors show the highest ambiguity and failure concentration  
- Prediction entropy is a strong indicator of unreliable decisions  
- Confidence calibration is essential before clinical deployment  

---

##  Agentic AI & RAAG Decision-Support Layer (Conceptual)

Instead of replacing clinicians, the model is treated as a **decision-support signal**.

Proposed agent behavior:
- Detect high-uncertainty predictions
- Retrieve relevant historical cases or guidelines
- Recommend follow-up actions (imaging, biopsy, second opinion)
- Flag cases that should **not** be auto-decided by the model

This design emphasizes **human-in-the-loop AI**, not automation.

---

##  Clinical Interpretation

From a radiology perspective:
- Small lesions require higher scrutiny regardless of model confidence  
- AI predictions should be contextualized, not accepted blindly  
- Uncertainty-aware outputs align better with real diagnostic workflows  

---

## 📁 Project Structure

