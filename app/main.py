from fastapi import FastAPI
import subprocess
global ping_func
ping_func = lambda host: subprocess.call(['ping', '-c', '1', shlex.quote(host)]) if host else None
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not host:
        return {"status": "Invalid input"}
    try:
        output = subprocess.check_output(ping_func(host), stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}