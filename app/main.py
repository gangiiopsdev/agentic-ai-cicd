from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess(command: list) -> str:
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        raise Exception(f'Command failed with return code {process.returncode}: {stderr}')
    return stdout

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_host = shlex.quote(host)
        result = safe_subprocess(['ping', '-c', '1', safe_host])  # Limit the number of pings for security
        return {'status': 'completed', 'output': result}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}