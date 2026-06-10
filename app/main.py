from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement a proper input sanitization function here
    return input_string.replace('ping', '').replace('-', '')

@app.get="/"
async def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
async def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}