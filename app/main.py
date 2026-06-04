from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(shlex.split(f'ping -c 1 {shlex.quote(sanitized_host)}'), stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode('utf-8')}"