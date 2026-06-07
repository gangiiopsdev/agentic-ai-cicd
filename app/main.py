from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', '-c', '4', host], stderr=subprocess.STDOUT, timeout=10)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    else:
        return {"status": "completed", "output": output.decode()}