from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'result': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)