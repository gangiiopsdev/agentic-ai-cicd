from fastapi import FastAPI
import subprocess
from os.path import abspath, dirname

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use absolute path for 'ping' command to avoid partial path issues
        full_path = abspath(dirname(__file__)) + '/ping'
        result = subprocess.run([full_path, host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}