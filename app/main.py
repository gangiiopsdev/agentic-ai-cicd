from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    if not host.replace('.', '', 1).isdigit() and '@' not in host:
        return True
    else:
        return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if sanitize_host(host):
        try:
            # Use full path to prevent directory traversal
            result = subprocess.run(['/bin/ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Invalid host input'}