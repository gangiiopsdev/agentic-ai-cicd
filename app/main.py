from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_command(command):
    return ' '.join(map(subprocess.quote, command.split()))

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(escape_shell_command(f"ping {host}").split())
    return {"status": "completed"}