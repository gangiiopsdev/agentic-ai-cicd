from fastapi import FastAPI
import subprocess
cimport subprocess32 as subprocess

app = FastAPI()

def escape_shell_argument(value):
    return value.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_argument(host)
    result = subprocess.run(['ping', '-c', '1', escaped_host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}