# Emotion-Aware-Movie-Recommendation-System

# 🎬 Emotion-Aware Movie Recommendation System

This project recommends movies based on the **user's emotional state**, detected from either **text** (using BERT) or **facial expressions** (using a CNN trained on FER2013).

---

## 🚀 Demo
A simple Flask API is used to take in text/image inputs and return movie recommendations based on detected emotion.

---

## 📌 Features
- Multi-modal emotion detection (NLP + CV)
- Emotion classification using BERT (GoEmotions)
- Facial expression recognition using CNN (FER2013)
- Hybrid content-based movie recommendation engine
- Flask API backend (can be containerized with Docker)

---


---

## 📂 Datasets

- **Text**: [GoEmotions (Simplified)](https://huggingface.co/datasets/google-research-datasets/go_emotions)
- **Image**: [FER2013](https://www.kaggle.com/datasets/msambare/fer2013)
- **Movies**: [MovieLens 100k](https://grouplens.org/datasets/movielens/)

---

## 🧠 Models

### 📝 Text Emotion Classifier
- Model: `BERT-base-uncased`
- Fine-tuned on: GoEmotions
- Output: One of 28 emotion classes


---

## 📦 `requirements.txt` 

```text
transformers
datasets
torch
tensorflow
pandas
flask
numpy
scikit-learn
Pillow


### 🖼️ Image Emotion Classifier
- CNN trained on FER2013 (7-class emotion recognition)

---

## ⚙️ How to Run

### 1. Clone this repo
```bash
git clone https://github.com/yourusername/emotion-aware-movie-recommender.git
cd emotion-aware-movie-recommender

