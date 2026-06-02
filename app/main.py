from fastapi import FastAPI
import subprocess
import shlex
def execute_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = shlex.split(f"ping {host}")
    output = execute_command(command)
    return {"status": "completed", "output": output}