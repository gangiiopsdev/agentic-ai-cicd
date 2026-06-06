from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use the shlex module to safely split the command string into a list of arguments
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)