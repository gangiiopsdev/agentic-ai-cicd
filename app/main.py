from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use safe alternatives like ping3 or check_output without shell=True
    try:
        result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return {'status': 'completed'}
        else:
            return {'status': 'failed', 'error': result.stderr.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if '@' in host or ':' in host or '%' in host:
        return {'status': 'failed', 'error': 'Invalid host format'}
    return safe_ping(host)