from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        args = ["ping", "-c", "1", shlex.quote(host)]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}

@app.get('/ping')
def ping(host: str):
    if not host.isnumeric() and '@' not in host:
        return safe_ping(host)
    else:
        return {'error': 'Invalid host', 'status': 'failed'}