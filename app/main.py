from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command: str):
    args = command.split()
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    command = f"ping {host}"
    execute_command(command)

    return {"status": "completed"}