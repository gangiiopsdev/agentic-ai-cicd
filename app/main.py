from fastapi import FastAPI
import subprocess
def safe_subprocess(args):
    try:
        completed_process = subprocess.run(args, check=True, capture_output=True, text=True)
        return completed_process.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    safe_args = [arg.strip() for arg in shlex.split(' '.join(args)) if arg.strip()]
    result = safe_subprocess(safe_args)
    return {"status": "completed", "output": result}