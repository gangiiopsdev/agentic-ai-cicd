from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(command: str):
    return ' '.join(subprocess.list2cmdline([arg]) for arg in command.split())

@app.get="/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(escape_command(f"ping {host}").split(), shell=False)
    return {"status": "completed"}