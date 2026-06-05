from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        response = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return response.stdout.decode()
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)