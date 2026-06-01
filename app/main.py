from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}, 403
    else:
        return {'status': 'error', 'message': 'Unauthorized host'}, 403