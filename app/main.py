from fastapi import FastAPI
import subprocess
def run_safe_ping(host):
    if '.' in host and '-' not in host:
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
            return {'status': 'completed', 'result': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return run_safe_ping(host)