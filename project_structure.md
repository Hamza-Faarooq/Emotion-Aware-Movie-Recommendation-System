emotion-aware-movie-recommender/
├── app/
│ ├── text_emotion.py # Predicts emotion from text using BERT
│ ├── image_emotion.py # Predicts emotion from face image (CNN on FER2013)
│ ├── recommend.py # Recommends movies based on detected emotion
│ ├── fusion.py # Combines text/image emotions
│ └── app.py # Flask API app entry point
├── models/ # Trained BERT and CNN models (or load scripts)
├── utils/
│ └── preprocessing.py # GoEmotions preprocessing + label mapping
├── templates/ # (Optional) Frontend HTML files
│ └── index.html
├── static/ # CSS, JS, image assets
├── data/ # MovieLens data / Sample images
├── requirements.txt # Python dependencies
├── Dockerfile # (Optional) For Docker deployment
├── README.md # Project documentation
└── .gitignore # Files to ignore (e.g. pycache, models)
