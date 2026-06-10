from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))[:255]

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"status": "error", "message": "Invalid host parameter"}
    try:
        subprocess.run(['ping', *shlex.split(sanitized_host)], capture_output=True, text=True, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}