from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    try:
        subprocess.check_call(['ping', host], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_wrapper(host: str):
    return ping(host)