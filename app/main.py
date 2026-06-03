from fastapi import FastAPI
import subprocess
global_params = '-c' if sys.platform == 'win32' else ''

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', global_params, host])
    return {"status": "completed"}