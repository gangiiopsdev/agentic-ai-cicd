from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
        if result.returncode == 0:
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'failed', 'output': result.stderr}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}