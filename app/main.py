from fastapi import FastAPI
import subprocess
globally_safe_ping = ['ping']

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(globally_safe_ping + [host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Ping failed with error: {e.stderr.decode('utf-8') if e.stderr else 'Unknown error'}"

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result}