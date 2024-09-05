import requests
import os

scriptPath = os.getcwd()


# Define the model endpoint and your API token
api_url = "https://api-inference.huggingface.co/models/bert-large-uncased-whole-word-masking-finetuned-squad"
headers = {"Authorization": "Bearer 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"}


def getAnswer(courseId, question):

    contextPath = os.path.join(scriptPath, 'chatbot/context', str(courseId), 'data.txt')
    context = ''

    with open(contextPath, 'r') as file:
        context = file.read()
    
    payload = {
        "inputs": {
            "question": question,
            "context": context
        }
    }

    response = requests.post(api_url, headers=headers, json=payload)
    result = response.json()

    return result
