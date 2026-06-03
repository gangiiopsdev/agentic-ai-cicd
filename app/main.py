from fastapi import FastAPI
import subprocess
def escape_shell_argument(value):
    return value.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_argument(host)
    subprocess.call(f"ping {escaped_host}", shell=False)
    return {"status": "completed"}