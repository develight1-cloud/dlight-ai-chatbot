from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from huggingface_hub import inference

app = FastAPI()

# Define request model
class Message(BaseModel):
    prompt: str

# Initialize inference client with your Hugging Face model
client = inference.InferenceApi(model='gpt2', token='YOUR_HUGGING_FACE_TOKEN')

@app.post("/chat")
async def chat(message: Message):
    try:
        # Get response from the Hugging Face model
        response = client(message.prompt)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))