from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.strip().replace('.', '', 1).isdigit():
        return False
    try:
        output = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if output.returncode != 0:
            return {'status': 'failed', 'error': output.stderr}
        else:
            return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result['status'] == 'failed':
        return result
    else:
        return result