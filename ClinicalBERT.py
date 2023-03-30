import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

# Load the pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("emilyalsentzer/Bio_ClinicalBERT")
model = AutoModelForTokenClassification.from_pretrained("emilyalsentzer/Bio_ClinicalBERT")

# Define the text to analyze
text = "The patient was diagnosed with hypertension and prescribed lisinopril. She was also ordered to get a blood test and an X-ray."

# Tokenize the text and run it through the model
inputs = tokenizer.encode(text, return_tensors="pt")
outputs = model(inputs).logits
predictions = torch.argmax(outputs, dim=2)

# Extract the entities and their labels
entities = []
for i, label in enumerate(predictions[0]):
    if label != 0:
        entity = {"entity": tokenizer.decode([inputs[0][i]]).strip(), "label": model.config.id2label[label.item()]}
        entities.append(entity)

# Print the entities and their labels
for entity in entities:
    print(entity["entity"], entity["label"])
