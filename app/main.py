from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input')
    # Sanitize the host to prevent shell injection
    sanitized_host = ''.join(filter(str.isalnum, host))
    return {'status': 'completed', 'output': safe_ping(sanitized_host)}