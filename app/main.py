from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(value):
    return value.replace(';', ' ').replace('&', ' ')  # Basic escaping for demonstration purposes

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_argument(host)
    subprocess.call(f"ping {safe_host}", shell=True)
    return {"status": "completed"}