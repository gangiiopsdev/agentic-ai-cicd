from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Use shlex.quote to ensure that the host parameter is properly escaped
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)