from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> dict:
    try:
        # Sanitize the host parameter
        sanitized_host = ''.join(filter(str.isalnum, host))
        output = subprocess.run(shlex.split(f'ping -c 4 {sanitized_host}'), capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e.stderr)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

@app.get("")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}