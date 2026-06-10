from fastapi import FastAPI
import subprocess
from urllib.parse import quote_plus

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', quote_plus(host)], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}