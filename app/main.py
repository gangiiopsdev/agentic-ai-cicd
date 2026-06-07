from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(c for c in host if c in allowed_chars)
    return sanitized
def execute_ping(host: str) -> int:
    try:
        command = shlex.split(f'ping {sanitize_host(host)}')
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e.stderr.decode()}')
        return 1
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    status = execute_ping(host)
    if status == 0:
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'error': f'Ping failed with return code {status}'}