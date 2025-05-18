from transformers import BertTokenizer, BertForSequenceClassification, TrainingArguments, Trainer
import torch
from sklearn.model_selection import train_test_split

# Split data into train/validation sets
train_df, val_df = train_test_split(data, test_size=0.2, random_state=42)

# Load BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Tokenize text
def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True, max_length=128)

train_encodings = tokenizer(train_df["text"].tolist(), truncation=True, padding=True, max_length=128)
val_encodings = tokenizer(val_df["text"].tolist(), truncation=True, padding=True, max_length=128)

# Convert to PyTorch datasets
class EmotionDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item["labels"] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

# Map emotion labels to unique IDs
unique_emotions = data["emotions"].unique().tolist()
train_labels = [unique_emotions.index(emotion) for emotion in train_df["emotions"]]
val_labels = [unique_emotions.index(emotion) for emotion in val_df["emotions"]]

train_dataset = EmotionDataset(train_encodings, train_labels)
val_dataset = EmotionDataset(val_encodings, val_labels)

model = BertForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=len(emotion_labels),
    problem_type="multi_label_classification"
)

# Training arguments
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./results",
    report_to="none",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    eval_strategy="epoch",  # Use this for newer library versions
    # evaluation_strategy="epoch",  # Use this if you're on transformers <4.4.0
    logging_dir="./logs",
    metric_for_best_model="f1",
)


# Train
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
)

trainer.train()

