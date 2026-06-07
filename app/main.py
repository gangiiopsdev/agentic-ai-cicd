from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_str: str) -> str:
    return ''.join(char for char in input_str if char.isalnum() or char in '._-')

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = quote(sanitize_input(host))
        subprocess.call(['ping', '-c', '1', sanitized_host], shell=False)  # Limiting the number of pings to one
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}