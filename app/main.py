from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(host):
    return ''.join(e for e in host if e.isalnum() or e in ['.', '@', '-'])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if '.' in sanitized_host and '@' not in sanitized_host:
        try:
            result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Invalid host input"}