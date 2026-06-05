from fastapi import FastAPI
import subprocess

def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_'
    return all(char in allowed_chars for char in host)

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if validate_host(host):
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "output": e.stderr}
    else:
        return {"status": "error", "output": "Invalid host name"}