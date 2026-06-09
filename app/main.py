from fastapi import FastAPI
import subprocess
import shlex
def safe_command(args):
    return subprocess.run(shlex.split(' '.join(args)), capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        if not host.isalnum():
            raise ValueError("Invalid host name")
        result = safe_command(['ping', shlex.quote(host)])
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "error": str(e)}