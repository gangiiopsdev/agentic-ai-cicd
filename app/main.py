from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    # Safe implementation using subprocess.run and list of args
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e}", 400

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)