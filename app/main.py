from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_str: str) -> str:
    return ''.join(char for char in input_str if char.isalnum() or char in '._-')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = quote(sanitize_input(host))
        command = ['ping', '-c', '1', sanitized_host]
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": subprocess.PIPE}
    except Exception as e:
        return {"error": str(e), "status": "failed"}