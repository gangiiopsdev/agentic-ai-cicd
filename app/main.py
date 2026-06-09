from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'stdout': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)