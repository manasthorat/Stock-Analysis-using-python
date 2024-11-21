# Predicting Trade Outcomes Using Machine Learning

This project aims to predict trade outcomes (Trade Result) using three key features: **RSI (Relative Strength Index)**, **Volume Multiple**, and **Market Cap**. The repository explores various machine learning models, evaluates their performance, and interprets the results to provide actionable insights.

---

## 📁 Project Structure

### **Stage 1: Data Filtering**
Analyze over 2,000 NSE-listed companies to identify stocks where the current day's trading volume exceeds four times the two-week average volume, leveraging data from Yahoo Finance.

### **Stage 2: Data Calculation and Backtesting**
- Calculate indicators such as RSI, volume multiple, and other relevant parameters.
- Store the results in a separate CSV file.
- Conduct backtesting to evaluate performance, including profit and loss outcomes.

### **Stage 3: Model Evaluation**
- Compare results using multiple machine learning models.
- Use RSI, volume multiple, and market capitalization as key features to predict trade outcomes.

### **Stage 4: Trade Prediction and Execution**
Deploy the best-performing model to:
- Predict the probability of profit for stocks meeting the predefined conditions.
- Execute trades based on the generated insights.

---

## 🛠️ Tools and Libraries

This project leverages the following tools and libraries:
- **Python**: Primary programming language.
- **Pandas**: For data manipulation and preprocessing.
- **Scikit-learn**: For machine learning models and feature analysis.
- **XGBoost**: Gradient boosting algorithm for classification.
- **SHAP**: To explain model predictions.
- **Matplotlib/Seaborn**: For data visualization.
- **PDPbox**: To analyze partial dependence of features.

---

## 🧪 Machine Learning Models Evaluated

- Logistic Regression  
- Random Forest  
- XGBoost  
- Neural Networks (Multi-Layer Perceptron)  
- Naive Bayes  
- Support Vector Machines (SVM) with probability calibration  
- Voting Classifier (ensemble approach)  

---

## 🔄 Workflow

### **Data Preprocessing**
- Handled missing and infinite values.
- Standardized the features using `StandardScaler`.

### **Model Training**
- Trained and evaluated multiple machine learning models.
- Tuned hyperparameters to improve performance.

### **Model Analysis**
- Evaluated metrics such as accuracy, precision, recall, F1 score, and AUC-ROC.
- Used **SHAP** and **PDP** for feature interpretability.

---

## 📊 Results

| Model                  | Accuracy | Precision | Recall | F1 Score | AUC-ROC |
|------------------------|----------|-----------|--------|----------|---------|
| Logistic Regression    | 0.5959   | 0.5959    | 1.0000 | 0.7468   | 0.5282  |
| Random Forest          | 0.5664   | 0.6118    | 0.7456 | 0.6721   | 0.5378  |
| XGBoost                | 0.5614   | 0.6030    | 0.7728 | 0.6774   | 0.5214  |
| Neural Networks (Tuned)| 0.6051   | 0.6093    | 0.9685 | 0.7516   | 0.5557  |
| Naive Bayes            | 0.4129   | 0.5805    | 0.0538 | 0.0984   | 0.5111  |
| SVM (Calibrated)       | 0.5956   | 0.5964    | 0.9941 | 0.7456   | 0.5113  |
| Voting Classifier      | 0.5909   | 0.5984    | 0.9532 | 0.7352   | 0.5398  |

**Key Takeaways:**
- Neural Networks outperformed other models after hyperparameter tuning.
- Logistic Regression, SVM, and Voting Classifier showed competitive results.
- Naive Bayes was unsuitable due to low recall and F1 score.

---

## 🔍 Feature Analysis

### **Feature Importance**
- **RSI**: The most significant predictor of trade outcomes.
- **Market Cap**: Strong influence with diminishing returns.
- **Volume Multiple**: Had a nonlinear effect.

### **Model Interpretability**
- **SHAP Analysis**:
  - RSI had a positive correlation with favorable trade results.
  - Market Cap showed a threshold effect beyond which impact plateaued.
- **Partial Dependence Plots**:
  - RSI exhibited a near-linear relationship with trade outcomes.
  - Volume Multiple had a complex impact pattern.

---

## 🚀 Future Work

- Add more features to capture broader market dynamics.
- Explore advanced deep learning models for further accuracy improvements.
- Implement time-series models if the dataset allows temporal analysis.

