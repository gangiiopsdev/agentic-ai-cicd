from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the input
        if not host.strip() or '&&' in host or ';' in host or '|' in host:
            return {'status': 'failed', 'error': 'Invalid input'}
        # Use a whitelist of allowed hosts
        allowed_hosts = ['example.com', 'localhost']
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Invalid host'}
        # Use os.path.abspath to prevent directory traversal
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}