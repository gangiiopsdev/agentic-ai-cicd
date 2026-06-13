from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, capture_output=True)
    return result.stdout.decode('utf-8').strip()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": result}
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr.decode('utf-8').strip()}}