from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    subprocess.call(['ping', host])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Using check_output to avoid shell=True and handle errors gracefully
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "result": result.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.output.decode('utf-8')}