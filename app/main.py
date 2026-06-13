from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Use shlex.quote to ensure that the host parameter is properly escaped
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, shell=False)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        return {'error': 'Invalid host parameter'}
    return safe_ping(host)