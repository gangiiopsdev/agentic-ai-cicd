from fastapi import FastAPI
import subprocess

def is_valid_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}

    # Validate and sanitize the host input before using it in subprocess
    sanitized_host = subprocess.list2cmdline(['ping', '-c', '1', host])
    try:
        result = subprocess.run(sanitized_host, check=True, timeout=5, capture_output=True, text=True, shell=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}