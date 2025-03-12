# 🚀 Named Entity Recognition (NER) Project - Entity Masking

## 📖 Project Overview
This project is built to extract and mask sensitive Named Entities (like phone numbers, emails, user IDs, and URLs) from a given text document using **Named Entity Recognition (NER)**. 

The model is **fine-tuned using Pre-trained Transformers (BERT)** to identify and mask these entities. A web app was also created using Flask to provide a user-friendly interface.

---

## ✅ Problem Statement
The goal of this project was to:
- 📜 Detect sensitive entities such as Phone Numbers, Emails, User IDs, and URLs from text.
- 🤖 Fine-tune a Pre-trained NER Model to enhance the entity masking.
- 💻 Build a web app to allow users to input text and mask sensitive data.

---

## ✅ Tools and Libraries Used
| Tool         | Purpose        |
|--------------|-----------------|
| Python       | Programming      |
| HuggingFace  | Pre-trained NER Models |
| Transformers | Deep Learning Model  |
| Pandas       | Data Processing   |
| Flask        | Web Application   |
| Sklearn      | Model Evaluation  |
| Matplotlib   | Data Visualization |
| Seaborn      | Confusion Matrix Plot |

---

## ✅ Dataset Used
The dataset was provided as a JSON file, consisting of:
- ✔ Text content
- ✔ Tokens and Labels
- ✔ Sensitive entities like emails, phone numbers, etc.

---

## ✅ Project Flow
1. 📊 **Data Preprocessing:** Loaded and tokenized the dataset.
2. 🤖 **Model Training:** Used Huggingface Pre-trained BERT Model for Named Entity Recognition (NER).
3. 🏗 **Fine-Tuning:** Fine-tuned the model on custom dataset to extract phone numbers, emails, user IDs, and URLs.
4. 💻 **Web Application:** Built a web app using Flask to take text input and mask sensitive data.
5. 📊 **Evaluation:** Evaluated the model using Classification Report and Confusion Matrix.

---

## ✅ Results
- 📊 **Confusion Matrix:** ![View Confusion Matrix](confusion_matrix.png)
- 📜 **Classification Report:** [Download Here](classification_report.csv)
- 📝 **Masked Data:** [Download Masked Data](Masked_Data.csv)

---

## ✅ Files Available in This Repository
| File Name            | Purpose                                                                 |
|---------------------|--------------------------------------------------------------------------|
| data_processing.py   | Preprocessing of text data                                              |
| model_training.py    | Fine-tuning the Huggingface NER Model                                   |
| app.py               | Flask Web Application                                                   |
| Masked_Data.csv      | Masked output data from the NER Model                                    |
| classification_report.csv | Evaluation Metrics for Model Accuracy                                 |
| confusion_matrix.png | Confusion Matrix Plot                                                   |
| Literature_Survey.pdf | Literature Survey Document                                              |
| Model_Limitations.pdf | Model Limitations Document                                              |
| Synthetic_Dataset.pdf | Synthetically Generated Dataset                                          |
| Final_Report.pdf     | Final Report Document                                                    |

---

## ✅ How to Run This Project Locally
Follow these steps to run the project on your local machine:

### 🚀 Step 1: Clone the Repository
```bash
git clone https://github.com/Nayanika2808/NER1_Project.git
cd NER1_Project

# Named Entity Recognition (NER) Web Application  

This is a Flask-based Named Entity Recognition (NER) web application that identifies and masks entities like phone numbers, emails, user IDs, and URLs from input text using `spaCy`.  

## 🚀 Live Demo  
[Click here to access the application](https://ner1-project.onrender.com)  

## 📌 Features  
- Detects and masks sensitive information (emails, phone numbers, etc.).  
- Uses `spaCy` for Named Entity Recognition (NER).  
- Simple and interactive web interface.  
- REST API support for programmatic access.  

## 🔹 How to Use  
1. Open the **[Live Demo](https://ner1-project.onrender.com)** link in your browser.  
2. Enter any text containing emails, phone numbers, or other entities.  
3. Click the **Submit** button to see the masked output.  

## 🛠 API Usage  
The NER model also supports API-based usage:  

**Endpoint:**  
```http
POST /ner

![image](https://github.com/user-attachments/assets/a3235721-f9df-4cb8-8f95-dd15444b2943)

