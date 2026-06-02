from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Basic sanitization to prevent simple injection attacks
    return ''.join(c for c in input_string if c.isalnum() or c in ['.', '-', '_'])

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}