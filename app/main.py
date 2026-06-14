from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input using a whitelist approach
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}