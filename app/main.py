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
        result = safe_ping(host)
        return {"status": f'Status Code: {result.returncode}, Output: {result.stdout}'}
    except ValueError as e:
        return {"error": str(e)}