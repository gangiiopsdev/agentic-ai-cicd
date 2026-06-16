from fastapi import FastAPI
import subprocess
import shlex
def shell_safe_input(value: str) -> bool:
    return value.isalnum() and len(value) <= 64

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not shell_safe_input(host):
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}