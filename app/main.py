from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if '.' in host:
        try:
            output = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'invalid_host'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)