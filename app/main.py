from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isnumeric():
        return 'Invalid input'
    return subprocess.run(['ping', host], capture_output=True, text=True).stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, str) and 'Invalid input' in result:
        return {'status': 'error', 'message': result}
    return {'status': 'completed', 'result': result}