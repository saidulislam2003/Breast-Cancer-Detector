# 🧬 Breast Cancer Detector

An interactive and intelligent web app that uses a Support Vector Machine (SVM) model to **predict the risk of breast cancer** based on diagnostic measurements. This application provides healthcare professionals and patients with a fast, simple, and reliable tool for early breast cancer detection.

🌐 **Live App**: [Click to Try it!](https://breast-cancer-detector-app.streamlit.app/)  
📁 **Repository**: [View on GitHub](https://github.com/saidulislam2003/Breast-Cancer-Detector)

---

## 🚀 Features

- 🎯 Built with **SVM**, achieving up to **97% accuracy** on the dataset.
- ⚡ **Real-time predictions** based on 10+ user input parameters.
- 📊 Clean, intuitive, and interactive **Streamlit interface**.
- 📁 Based on the **Wisconsin Breast Cancer Dataset**.
- ✅ Pre-trained model to ensure fast predictions without delay.
- 🔒 No user data is stored — privacy respected.

---

## 📌 How It Works

1. User enters diagnostic details (mean radius, texture, perimeter, etc.)
2. The app scales the input and feeds it to the **SVM model**.
3. The model predicts:
   - **Benign (0)** — Low risk
   - **Malignant (1)** — High risk
4. Result is displayed instantly on the web interface.

---

## 🛠️ Technologies Used

| Tool/Library     | Purpose                          |
|------------------|----------------------------------|
| Python 🐍        | Main programming language        |
| Scikit-learn     | Machine Learning (SVM)           |
| Streamlit        | Web App Frontend                 |
| Joblib           | Model Serialization              |
| Pandas & NumPy   | Data Handling                    |
| Matplotlib       | Visualization (EDA)              |

---

## 🧪 Model Performance

- 🔍 **Accuracy**: 97%
- 📈 Model: **SVC (Support Vector Classifier)**
- 🔬 Feature Scaling: **StandardScaler**
- 💾 Model trained and saved with `joblib`

---

## 🖥️ Run Locally

1. **Clone the repo**:
   ```bash
   git clone https://github.com/saidulislam2003/Breast-Cancer-Detector.git
   cd Breast-Cancer-Detector
2. **Create a virtual environment (optional but recommended)**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```
   streamlit run streamlit_app.py
   ```
