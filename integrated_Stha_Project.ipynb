# Insurance Fraud Detection Project Notebook Template

## 1. Project Setup

### 1.1. Import Required Libraries
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
```

### 1.2. Load Dataset
```python
# Load the dataset
data = pd.read_csv('insurance_data.csv')

# Display basic information
data.info()
data.head()
```

---

## 2. Data Exploration and Cleaning

### 2.1. Summary Statistics
```python
# General statistics
data.describe()

# Check for missing values
print(data.isnull().sum())
```

### 2.2. Data Visualization
```python
# Visualize the distribution of fraud vs. non-fraud
sns.countplot(x='fraud_reported', data=data)
plt.title('Fraud Reported Distribution')
plt.show()

# Analyze correlations among numerical features
plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Matrix')
plt.show()
```

### 2.3. Handle Missing Values
```python
# Example: Replace missing values in 'property_damage' with the mode
data['property_damage'] = data['property_damage'].fillna(data['property_damage'].mode()[0])

# Verify no missing values remain
print(data.isnull().sum())
```

### 2.4. Encode Categorical Variables
```python
# Use LabelEncoder for categorical columns
label_encoders = {}
for column in ['insured_sex', 'insured_education_level', 'insured_occupation', 'insured_hobbies', 'policy_state', 'incident_state', 'incident_city', 'collision_type', 'police_report_available']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le
```

---

## 3. Feature Engineering

### 3.1. Create New Features
```python
# Example: Create claim-to-premium ratio
data['claim_to_premium_ratio'] = data['total_claim_amount'] / data['policy_annual_premium']
```

### 3.2. Feature Selection
```python
# Select relevant features and target
features = [
    'age', 'policy_annual_premium', 'umbrella_limit', 'number_of_vehicles_involved',
    'bodily_injuries', 'witnesses', 'total_claim_amount', 'claim_to_premium_ratio'
]
target = 'fraud_reported'

X = data[features]
y = data[target]
```

---

## 4. Model Development

### 4.1. Split Data
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

### 4.2. Scale Features
```python
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

### 4.3. Train Model
```python
# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
```

---

## 5. Model Evaluation

### 5.1. Performance Metrics
```python
# Make predictions
y_pred = model.predict(X_test)

# Classification report
print(classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.show()
```

### 5.2. ROC-AUC Curve
```python
# Calculate ROC-AUC
y_pred_prob = model.predict_proba(X_test)[:, 1]
roc_auc = roc_auc_score(y_test, y_pred_prob)

# Plot ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
```

---

## 6. Conclusion and Next Steps

### 6.1. Insights
- Summari
ze key findings from the model evaluation.

### 6.2. Recommendations
- Discuss potential improvements (e.g., collect more data, use other models).

### 6.3. Deployment
- Outline steps to deploy the fraud detection system into production.
