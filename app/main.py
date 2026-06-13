from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(command):
    return command.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    safe_host = escape_command(host)
    subprocess.call(f"ping {safe_host}", shell=False)

    return {"status": "completed"}