from fastapi import FastAPI
import subprocess
gapp = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Input validation to prevent injection attacks and DoS
    try:
        host = int(host)
    except ValueError:
        return {'status': 'failed', 'error': 'Invalid input'}
    if not 0 < host < 256 or len(str(host)) > 15:
        return {'status': 'failed', 'error': 'Invalid input'}
    args = ["ping", "-c", "4", str(host)]  # Use list instead of shlex.split to avoid shell injection
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}