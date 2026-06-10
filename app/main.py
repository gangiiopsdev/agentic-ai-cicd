from fastapi import FastAPI
import subprocess
def safe_subprocess(command, *args):
    return subprocess.check_output([command] + list(args), timeout=5, stderr=subprocess.STDOUT)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_subprocess('ping', host, shell=False)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}