from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation for 'host'
    if not host or len(host) > 255:
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(['/bin/ping', subprocess.check_output(['ping', '-c1', host], stderr=subprocess.STDOUT, text=True)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}