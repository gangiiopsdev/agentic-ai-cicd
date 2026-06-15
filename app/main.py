from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_command(command):
    return ' '.join(subprocess.list2cmdline(arg) for arg in command.split())

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    subprocess.call(escape_shell_command(f"ping {host}").split(), shell=False)
    return {"status": "completed"}