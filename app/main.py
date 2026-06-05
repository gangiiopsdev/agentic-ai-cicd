from fastapi import FastAPI
import subprocess
generate_random_command = ['ping', '8.8.8.8']  # Replace with a safe command or remove the function

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    subprocess.call(generate_random_command)  # Use a predefined command instead of user input
    return {"status": "completed"}