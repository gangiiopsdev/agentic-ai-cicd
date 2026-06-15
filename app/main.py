from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    ping_command = ['ping', host]
    try:
        result = subprocess.run(ping_command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    status = execute_ping(host)
    return {"status": status}