from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

app = FastAPI()

@app.get="/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)