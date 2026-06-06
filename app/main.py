from fastapi import FastAPI, HTTPException
import subprocess

def execute_ping(host):
    # Validate the host input to prevent command injection
    if not all(c.isalnum() or c in '-.' for c in host):
        raise HTTPException(status_code=400, detail='Invalid input')
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=e.stderr)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping(host: str):
    return execute_ping(host)