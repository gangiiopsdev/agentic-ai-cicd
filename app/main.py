from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', subprocess.list2cmdline([host])], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent shell injection
    if any(char in host for char in ['&&', ';', '|']):
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(subprocess.list2cmdline([host]))