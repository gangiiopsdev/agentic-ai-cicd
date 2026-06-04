from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit() or e in ['-', '.', '_', '/', ':', '@'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.run with shell=False and passing arguments separately
    result = subprocess.run(['ping', shlex.quote(sanitized_host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}