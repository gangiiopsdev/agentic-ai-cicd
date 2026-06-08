from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize and validate the input to mitigate command injection
        if not all(c.isalnum() or c in '.-' for c in host):  # Basic validation
            return {'status': 'failed', 'error': 'Invalid input'}
        host = shlex.quote(host)  # Use shlex.quote to escape special characters
        result = subprocess.run(['ping', host], check=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}