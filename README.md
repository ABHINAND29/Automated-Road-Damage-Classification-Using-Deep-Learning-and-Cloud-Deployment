# 🛣️ Road Damage Detection using Deep Learning

## 📌 Project Overview

Road infrastructure is a vital component of transportation systems and economic development. Poor road conditions, such as potholes, cracks, and surface deterioration, can lead to vehicle damage, increased maintenance costs, traffic congestion, and serious road accidents. Traditional road inspection methods rely on manual surveys, which are time-consuming, costly, and susceptible to human error.

This project presents a Deep Learning-based Road Damage Detection System capable of automatically classifying road surface images into different damage categories. The application provides real-time predictions through a user-friendly web interface, enabling faster and more accurate road condition assessment.

## 🎯 Project Objectives

Develop an intelligent system for automatic road damage classification.<br/>
Detect different road surface conditions using deep learning.<br/>
Reduce the dependency on manual road inspections.<br/>
Provide real-time predictions from uploaded road images.<br/>
Build a lightweight and interactive web application for end users.<br/>

## 🚀 Features

Upload road surface images.<br/>
Real-time road damage classification.<br/>
Multi-class image classification.<br/>
Confidence score for predictions.<br/>
Damage-specific maintenance recommendations.<br/>
Easy-to-use Streamlit web application.<br/>
Lightweight deployment suitable for real-world applications.<br/>


## 🛣️ Damage Categories

### The model classifies images into the following categories:

🕳️ Pothole
🛠️ Man-made Pothole
✅ No Pothole

📂 Dataset

Dataset: Road Damage Dataset (RDD2020 / RDD2022)

The dataset consists of road images captured using:

Smartphone cameras<br/>
Vehicle-mounted cameras<br/>
Image Preprocessing<br/>
Resize images to 224 × 224<br/>
Normalize pixel values (0–1)<br/>
Data augmentation<br/>
Rotation<br/>
Horizontal Flip<br/>
Brightness Adjustment<br/>
Zoom<br/>
Train / Validation / Test split<br/>
Handle class imbalance using class weights<br/>

## 🧠 Deep Learning Models

The following models were implemented and evaluated:

Baseline CNN<br/>
Custom Convolutional Neural Network<br/>
Used as the baseline model for comparison<br/>
Transfer Learning Models<br/>
MobileNetV2<br/>
ResNet50<br/>
EfficientNetB0<br/>

Transfer learning improves classification accuracy while reducing training time by leveraging pre-trained ImageNet weights.


## ⚙️ Technologies Used

#### Programming Language<br/>
Python<br/>
#### Libraries<br/>
TensorFlow<br/>
Keras<br/>
NumPy<br/>
OpenCV<br/>
Pillow<br/>
Matplotlib<br/>
Scikit-learn<br/>
Pandas<br/>
#### Web Framework<br/>
Streamlit<br/>

## 📊 Model Evaluation Metrics

### The models were evaluated using:

>Accuracy<br/>
>Precision<br/>
>Recall<br/>
>F1-Score<br/>
>Confusion Matrix<br/>
>Classification Report<br/>

## 🌐 Web Application Features

The Streamlit application includes:

Upload road surface images<br/>
Real-time prediction<br/>
Confidence score display<br/>
Damage-specific recommendation<br/>
Probability score for each class<br/>
Responsive user interface<br/>

Example:

Detected : Pothole

Confidence : 97.84%

Recommended Action :
Schedule immediate repair.

High risk of vehicle damage and accidents.

## Business Use Cases:
• Municipal Authorities: Prioritize road maintenance and repair activities<br/>
• Smart City Platforms: Automated road condition monitoring<br/>
• Transportation Departments: Safety assessment and reporting<br/>
• Educational Use: Demonstrate AI applications in infrastructure management<br/>
• Public Users: Report road damage using mobile-captured images<br/>

Road_Damage_Detection/


>│<br/>
>├── app.py<br/>
>├── road_damage_classifier.keras<br/>
>├── requirements.txt<br/>
>├── README.md<br/>
>│<br/>
>├── data/<br/>
>│   ├── train/<br/>
>│   ├── validation/<br/>
>│   └── test/<br/>
>│<br/>
>├── notebooks/<br/>
>│   └── model_training.ipynb<br/>
>│<br/>
>├── models/<br/>
>    ├── baseline_cnn.keras<br/>
>    ├── mobilenet.keras<br/>
>    ├── resnet50.keras<br/>
>    └── efficientnet.keras<br/>

## ▶️ Installation

Clone the repository:

git clone https://github.com/ABHINAND29/Automated-Road-Damage-Classification-Using-Deep-Learning-and-Cloud-Deployment.git

Navigate to the project folder:

cd road-damage-detection

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

## 📈 Future Enhancements
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
