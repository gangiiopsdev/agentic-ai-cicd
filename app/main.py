from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safer implementation using subprocess.run()
    try:
        result = subprocess.run(['ping', host], check=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)