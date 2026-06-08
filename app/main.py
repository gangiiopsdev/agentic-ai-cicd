from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    # Add additional sanitization logic if needed
    return input_str

@app.get('/ping')
def ping(host: str):
    try:
        safe_host = shlex.quote(sanitize_input(host))
        result = subprocess.run(['ping', '-c', '1'] + [safe_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}