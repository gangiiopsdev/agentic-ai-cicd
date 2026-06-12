from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['-', '_', '.', ':'])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = f'ping {shlex.quote(sanitized_host)}'
    result = subprocess.run(command, capture_output=True, text=True, check=False, shell=True)
    return {"status": "completed", "output": result.stdout}