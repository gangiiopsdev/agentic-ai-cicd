from fastapi import FastAPI
import subprocess
import shlex

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c == '.').strip()

def safe_ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(shlex.split(f'ping {sanitized_host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)