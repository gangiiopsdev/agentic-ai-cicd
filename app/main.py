from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    # Implement a more robust sanitization function here
    return ''.join(char for char in input_string if char.isalnum() or char in ['-', '.', '_', ':', '@'])

@app.get('/ping')
def ping(host: str):
    sanitized_host = shlex.quote(sanitize_input(host))
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}