from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_input(host):
    return ''.join(filter(str.isalnum, host))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = sanitize_input(host)
    if '.' in sanitized_host:
        result = subprocess.run(['ping', re.escape(sanitized_host)], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "error", "message": "Invalid input"}