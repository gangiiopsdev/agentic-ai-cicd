from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/`")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}