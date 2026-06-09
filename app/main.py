from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', '-', '_'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        command = shlex.split(f'ping {sanitized_host}')
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}