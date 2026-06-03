from fastapi import FastAPI
import subprocess
import shlex

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return False, "Host not allowed"
    return True, None

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    is_valid, message = validate_host(host)
    if not is_valid:
        return {'status': 'error', 'message': message}
    result = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}