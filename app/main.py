from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input before using it in the subprocess call
    safe_host = subprocess.list2cmdline([host])
    try:
        result = subprocess.run(['ping', '-c', '1', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}