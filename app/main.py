from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c.isspace())
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {shlex.quote(sanitized_host)}')
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}