from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command: str):
    result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    output = execute_command(command)
    return {"status": "completed", "output": output}