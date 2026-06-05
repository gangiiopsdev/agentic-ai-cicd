from fastapi import FastAPI
import subprocess
git_path = '/usr/bin/ping'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run([git_path, host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}