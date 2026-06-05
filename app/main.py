from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return subprocess.list2cmdline([arg])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host')
    try:
        output = subprocess.check_output(['ping', '-c', '1', escape_shell_arg(host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'error', 'error': str(e)}