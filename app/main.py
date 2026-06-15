from fastapi import FastAPI
import subprocess
given_host = 'example.com' # Replace this with a safe value or use input validation

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    subprocess.call(['ping', given_host])

    return {"status": "completed"}