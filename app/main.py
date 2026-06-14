from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Sanitize input to prevent injection attacks
    safe_host = ''.join(filter(str.isdigit, host))  # Only allow digits for simplicity
    try:
        command = ['ping', '-c', '1'] + shlex.split(safe_host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)