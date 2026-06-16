from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        command = ['ping', host]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    return {"status": safe_ping(host)}