from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_command(command):
    return [arg.strip() for arg in command.split(' ')] if isinstance(command, str) else command

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    subprocess.call(escape_shell_command(f"ping {host}"))
    return {"status": "completed"}