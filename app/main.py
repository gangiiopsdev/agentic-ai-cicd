from fastapi import FastAPI
import subprocess
import shlex

def sanitize_input(input_string):
    # Basic sanitization: remove non-alphanumeric characters and spaces
    return ''.join(e for e in input_string if e.isalnum() or e.isdigit())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = shlex.quote(sanitize_input(host))
    # Safe implementation with sanitization and additional checks
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}