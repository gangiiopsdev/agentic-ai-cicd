from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in '-.')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if all(c.isalnum() or c in '-.' for c in sanitized_host) and len(sanitized_host) <= 255:
        try:
            result = subprocess.run(shlex.split(f'ping -c 1 {sanitized_host}'), capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': e.stderr}
    return {'status': 'invalid_input'}