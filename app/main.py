from fastapi import FastAPI
import subprocess
import shlex
def secure_ping(host: str):
    try:
        command = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e.output)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}