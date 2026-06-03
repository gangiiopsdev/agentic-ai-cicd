from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['127.0.0.1', '::1']

@app.get("/ping")
def ping(host: str):
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True)
            return {'status': 'completed', 'result': result.stdout}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}