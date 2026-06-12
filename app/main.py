from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        if output.returncode == 0:
            return {'status': 'completed', 'output': output.stdout}
        else:
            return {'status': 'failed', 'error': output.stderr}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}