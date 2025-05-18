
import pandas as pd
from datasets import load_dataset

# Load the full GoEmotions dataset (simplified version)
dataset = load_dataset("google-research-datasets/go_emotions", "simplified")
# Access training split
train_data = dataset["train"]
# Show example
print(train_data[0])
# Assuming train_data is your loaded Hugging Face Dataset object
data = pd.DataFrame(train_data)
data

print(data.head())
print(data['labels'].value_counts())

# emotional label
# Get emotion labels from the dataset's metadata
emotion_labels = train_data.features["labels"].feature.names
# Convert label indices to emotion names
data["emotions"] = data["labels"].apply(lambda x: [emotion_labels[i] for i in x])
data = data.explode("emotions")  # Split rows with multiple labels
data = data[["text", "emotions"]]  # Keep only relevant columns
print(data.head())
