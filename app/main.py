from fastapi import FastAPI
import subprocess
import shlex
import re

global_input_re = re.compile(r'[^a-zA-Z0-9]')

app = FastAPI()

def sanitize_input(input_string):
    return global_input_re.sub('', input_string)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}