from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate the host input to avoid command injection
        if not all(c.isalnum() or c in ['-', '.'] for c in host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)