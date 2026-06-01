from fastapi import FastAPI
import subprocess
def execute_safe_command(command, *args):
    if not all(arg.isalnum() for arg in args):
        raise ValueError("Invalid argument")
    subprocess.call([command] + list(args))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    execute_safe_command("ping", host)
    return {"status": "completed"}