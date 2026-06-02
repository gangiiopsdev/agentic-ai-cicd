from fastapi import FastAPI
import subprocess
import asyncio

app = FastAPI()

def secure_ping(host: str):
    try:
        output = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            raise subprocess.CalledProcessError(output.returncode, 'ping', output.stderr.decode())
        return {'status': 'completed', 'output': stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isdigit():  # Basic validation to prevent command injection
        raise ValueError('Invalid input')
    # Sanitize the host parameter to avoid shell injection
    safe_host = subprocess.list2cmdline([host])
    return secure_ping(safe_host)