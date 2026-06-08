from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['-', '.', '_'] and not any(c.isdigit() for c in e))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = quote(sanitize_input(host), safe='/-._')
    command = ["ping", sanitized_host]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}