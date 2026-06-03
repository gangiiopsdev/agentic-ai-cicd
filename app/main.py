from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize the host input to prevent injection attacks
        if not all(c.isalnum() or c in '._-' for c in host):
            return {'status': 'error', 'message': 'Invalid hostname'}
        result = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}