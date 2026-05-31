from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Implement input sanitization logic here
    return input_str.strip()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', '-c', '1', sanitized_host])  # Use -c to limit the number of pings

    return {"status": "completed"}