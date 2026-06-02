from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True)
        return output
    except Exception as e:
        return str(e)

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    return {"status": safe_ping(host)}