from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(cmd: str) -> str:
    return ' '.join([subprocess.quote(arg) for arg in cmd.split()])

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = escape_command(f"ping {host}")
    subprocess.call(command, shell=True)

    return {"status": "completed"}