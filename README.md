🛣️ Road Damage Detection using Deep Learning

📌 Project Overview

Road infrastructure is a vital component of transportation systems and economic development. Poor road conditions, such as potholes, cracks, and surface deterioration, can lead to vehicle damage, increased maintenance costs, traffic congestion, and serious road accidents. Traditional road inspection methods rely on manual surveys, which are time-consuming, costly, and susceptible to human error.

This project presents a Deep Learning-based Road Damage Detection System capable of automatically classifying road surface images into different damage categories. The application provides real-time predictions through a user-friendly web interface, enabling faster and more accurate road condition assessment.

🎯 Project Objectives

Develop an intelligent system for automatic road damage classification.
Detect different road surface conditions using deep learning.
Reduce the dependency on manual road inspections.
Provide real-time predictions from uploaded road images.
Build a lightweight and interactive web application for end users.

🚀 Features

Upload road surface images.
Real-time road damage classification.
Multi-class image classification.
Confidence score for predictions.
Damage-specific maintenance recommendations.
Easy-to-use Streamlit web application.
Lightweight deployment suitable for real-world applications.


🛣️ Damage Categories

The model classifies images into the following categories:

🕳️ Pothole
🛠️ Man-made Pothole
✅ No Pothole

📂 Dataset

Dataset: Road Damage Dataset (RDD2020 / RDD2022)

The dataset consists of road images captured using:

Smartphone cameras
Vehicle-mounted cameras
Image Preprocessing
Resize images to 224 × 224
Normalize pixel values (0–1)
Data augmentation
Rotation
Horizontal Flip
Brightness Adjustment
Zoom
Train / Validation / Test split
Handle class imbalance using class weights

🧠 Deep Learning Models

The following models were implemented and evaluated:

Baseline CNN
Custom Convolutional Neural Network
Used as the baseline model for comparison
Transfer Learning Models
MobileNetV2
ResNet50
EfficientNetB0

Transfer learning improves classification accuracy while reducing training time by leveraging pre-trained ImageNet weights.


⚙️ Technologies Used

Programming Language
Python
Libraries
TensorFlow
Keras
NumPy
OpenCV
Pillow
Matplotlib
Scikit-learn
Pandas
Web Framework
Streamlit

📊 Model Evaluation Metrics

The models were evaluated using:

Accuracy
Precision
Recall
F1-Score
Confusion Matrix
Classification Report
🌐 Web Application Features

The Streamlit application includes:

Upload road surface images
Real-time prediction
Confidence score display
Damage-specific recommendation
Probability score for each class
Responsive user interface

Example:

Detected : Pothole

Confidence : 97.84%

Recommended Action :
Schedule immediate repair.

High risk of vehicle damage and accidents.

Business Use Cases:
• Municipal Authorities: Prioritize road maintenance and repair activities
• Smart City Platforms: Automated road condition monitoring
• Transportation Departments: Safety assessment and reporting
• Educational Use: Demonstrate AI applications in infrastructure management
• Public Users: Report road damage using mobile-captured images

Road_Damage_Detection/


│
├── app.py

├── road_damage_classifier.keras

├── requirements.txt

├── README.md

│

├── data/

│   ├── train/

│   ├── validation/

│   └── test/

│

├── notebooks/

│   └── model_training.ipynb

│

├── models/

    ├── baseline_cnn.keras

    ├── mobilenet.keras

    ├── resnet50.keras
    
    └── efficientnet.keras

▶️ Installation

Clone the repository:

git clone https://github.com/ABHINAND29/Automated-Road-Damage-Classification-Using-Deep-Learning-and-Cloud-Deployment

Navigate to the project folder:

cd road-damage-detection

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

📈 Future Enhancements
Grad-CAM visualization for model explainability.
Severity estimation of detected damage.
GPS-based road damage reporting.
Mobile application integration.
Real-time video detection.
Cloud deployment for public access.
Automatic maintenance prioritization.

👨‍💻 Author

Abhinand K M

Aspiring Data Scientist | Machine Learning Enthusiast
