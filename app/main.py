from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use a safe method to ping without invoking the shell
        output = subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}