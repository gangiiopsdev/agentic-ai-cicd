from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Using check_output and avoiding shell=True
    result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
    return {'status': 'completed', 'result': result.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)