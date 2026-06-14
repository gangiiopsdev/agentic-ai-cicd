from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()


def sanitize_input(user_input):
    return shlex.quote(user_input)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        # Safer implementation using subprocess.run without shell=True
        result = subprocess.run(['ping', '-c 1', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}