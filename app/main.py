from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c == '-').strip()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host or '-' not in sanitized_host:
        raise ValueError('Invalid hostname')
    result = subprocess.run(['ping', shlex.quote(sanitized_host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}