from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        response = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return response.stdout.decode('utf-8')
    except Exception as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}