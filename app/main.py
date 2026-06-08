from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use subprocess.Popen instead of shell=True for better security
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return f'Failed to ping {host}: {e.stderr.decode()}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)