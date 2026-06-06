from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(value):
    return value.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_argument(host)
    subprocess.run(['ping', escaped_host], check=True)
    return {"status": "completed"}