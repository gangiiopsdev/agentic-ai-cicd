from fastapi import FastAPI
import subprocess
import re
def sanitize_host(host: str) -> str:
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    return host
def escape_shell_arg(arg: str) -> str:
    return subprocess.list2cmdline([arg])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
        result = subprocess.run(['ping', '-c', '1', escape_shell_arg(sanitized_host)], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}