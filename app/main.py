from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host.strip())  # Remove leading/trailing whitespace and sanitize
        command = shlex.split(f'ping {sanitized_host}')  # Use shlex to safely split the command string
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}