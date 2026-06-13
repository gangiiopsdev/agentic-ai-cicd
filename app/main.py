from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_command(command: str):
    return command.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_command(host)
    # Safer implementation
    subprocess.call(f"ping {safe_host}", shell=False)
    return {"status": "completed"}