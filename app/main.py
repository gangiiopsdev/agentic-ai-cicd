from fastapi import FastAPI
import subprocess
c import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        args = shlex.split(f'ping -c 1 {host}')  # Limit the number of pings to reduce potential DoS
        subprocess.run(args, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}