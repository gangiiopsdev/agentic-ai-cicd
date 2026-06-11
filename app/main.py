from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', '-', '_'))

def run_ping(host):\n    safe_host = sanitize_input(host)\n    result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True)\n    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    return run_ping(host)