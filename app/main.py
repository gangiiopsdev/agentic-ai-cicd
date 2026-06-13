from fastapi import FastAPI
import subprocess
def ping(host: str):
    output = subprocess.run(['ping', host], capture_output=True, text=True)
    if output.stderr:
        return {'status': 'error', 'error': output.stderr}
    else:
        return {'status': 'completed', 'output': output.stdout}
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping_endpoint(host: str):
    result = ping(host)
    return result