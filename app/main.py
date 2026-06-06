from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        args = ['ping', host]
        result = subprocess.run(args, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)