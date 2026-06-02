from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize the host input to avoid command injection
        if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
            return {'status': 'failed', 'error': 'Invalid host'}
        args = shlex.split(f'ping {host}')
        output = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}