from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.strip() and all(c.isalnum() or c in '-.' for c in host):  # Basic validation
        try:
            result = subprocess.run(['ping', host], check=True, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'success', 'result': result.stdout.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e.stderr.decode('utf-8'))}
    else:
        return {'status': 'error', 'message': 'Invalid host'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)