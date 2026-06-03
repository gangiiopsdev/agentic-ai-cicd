from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    return ''.join(c if c.isalnum() or c in '-.' else '_' for c in host)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = shlex.split(f'ping -c 1 {shlex.quote(sanitized_host)}')
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}