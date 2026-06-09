from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    if not all(c.isalnum() or c in '.-' for c in input_str):  # Basic validation
        return False
    return True

@app.get('/ping')
def ping(host: str):
    try:
        if not sanitize_input(host):
            return {'status': 'failed', 'error': 'Invalid input'}
        host = shlex.quote(host)  # Use shlex.quote to escape special characters
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}