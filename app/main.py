from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host if host in allowed_hosts else None

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host:
        try:
            result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, shell=False)
            return {'status': 'completed', 'result': result.stdout}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}