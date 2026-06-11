from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ['.', '-', '_'])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        command = shlex.split(f'ping -c 1 {sanitized_host}')
        output = subprocess.check_output(command, timeout=10, stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode('utf-8')}