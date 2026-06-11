from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'stdout': result.stdout, 'stderr': result.stderr}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str): 
    return ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}