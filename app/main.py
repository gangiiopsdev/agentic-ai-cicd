from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.strip().isnumeric():
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Invalid input')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": f'Status Code: {result.returncode}, Output: {result.stdout}'}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}