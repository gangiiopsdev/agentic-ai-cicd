from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ['ping', host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.call(generate_ping_command(host))
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}