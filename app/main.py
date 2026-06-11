from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    try:
        # Use check_output to avoid shell=True and provide a timeout for safety
        subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "result": "Success"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}