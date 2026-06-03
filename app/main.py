from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Using subprocess.run instead of subprocess.call and avoiding shell=True
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr.decode()}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)