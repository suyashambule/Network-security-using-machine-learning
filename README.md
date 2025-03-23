# Network Security for Phishing Detection

## 📌 Overview
This project focuses on **phishing detection** using **machine learning**, enhancing network security by identifying fraudulent websites and emails. It implements an **end-to-end MLOps pipeline** for scalable deployment and real-time monitoring.

## 🚀 Features
- **Phishing Detection Model:** Uses machine learning to classify URLs/emails as phishing or legitimate.
- **End-to-End MLOps Integration:** Automated model training, validation, and deployment.
- **Real-time Monitoring:** Continuous logging and model performance tracking.
- **Scalable Deployment:** Dockerized application with GitHub Actions for CI/CD.

## 🛠️ Tech Stack
- **Programming:** Python, Scikit-learn, Pandas, NumPy
- **MLOps Tools:** MLflow, DagsHub, Docker, GitHub Actions, YAML
- **Deployment:** Cloud-based deployment for real-time inference

## 🔧 Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/suyashambule/Network-security-using-machine-learning.git
   cd Network-security-using-machine-learning
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the model training script:
   ```bash
   python train_model.py
   ```
4. Deploy the model using Docker:
   ```bash
   docker build -t phishing-detector .
   docker run -p 5000:5000 phishing-detector
   ```

## 📊 Results
- Achieved **94% accuracy**, reducing false positives.
- Improved phishing detection **reliability and security**.

## 📜 Usage
- Provide a URL or email as input to the model.
- The system classifies whether it is **phishing or legitimate**.
- Can be integrated into **network security frameworks** for automated protection.

## 🤝 Contributing
Feel free to submit issues or pull requests to enhance the project.

## 📄 License
This project is licensed under the **MIT License**.

## 📞 Contact
👤 **Suyash Ambule**  
📧 Email: [ambulesuyash@gmail.com](mailto:ambulesuyash@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/suyash-ambule](http://www.linkedin.com/in/suyash-ambule)  

