from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return any(host.startswith(allowed) for allowed in allowed_hosts)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not sanitize_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', f'/bin/ping {host}'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}