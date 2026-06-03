from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    ping_command = ['ping', host]
    result = subprocess.run(ping_command, capture_output=True, text=True)
    return result.stdout

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "failed", "error": str(e)}