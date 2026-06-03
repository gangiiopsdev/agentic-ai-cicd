from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safer implementation using subprocess.run with check=True and shell=False
    try:
        result = subprocess.run(['ping', host], check=True, shell=False, capture_output=True, text=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}