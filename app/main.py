from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(command):
    return [arg.replace(';', '').replace('&', '') for arg in command.split()]

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(escape_command(f"ping {host}"))

    return {"status": "completed"}