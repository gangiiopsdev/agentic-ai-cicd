from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use subprocess.run to avoid shell injection
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {
            'status': 'completed',
            'stdout': result.stdout,
            'stderr': result.stderr
        }
    except Exception as e:
        return {'error': str(e)}