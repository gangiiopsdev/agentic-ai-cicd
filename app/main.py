from fastapi import FastAPI
import subprocess
import shlex
def execute_command(command: str):
    args = ['ping'] + shlex.split(command)
    try:
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=10, shell=False)
        return True, output.decode()
    except subprocess.CalledProcessError as e:
        return False, e.output.decode()
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    success, output = execute_command(host)
    if success:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": output}