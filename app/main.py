from fastapi import FastAPI
import subprocess
def sanitize_host(host: str) -> str:
    # Add sanitization logic here (e.g., whitelist allowed hosts)
    return 'localhost' if host == 'localhost' else ''

app = FastAPI()

@app.get('/ping')
def ping():
    try:
        result = subprocess.run(['ping', 'localhost'], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}