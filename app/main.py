from fastapi import FastAPI
import subprocess
import shlex
def execute_command(command: str):
    args = shlex.split(command)
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode()}"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    result = execute_command(command)
    return {"status": "completed", "result": result}