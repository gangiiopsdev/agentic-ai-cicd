from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using list for args
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        return {'result': safe_ping(host)}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}