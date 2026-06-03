from fastapi import FastAPI
import subprocess
class SafePing:
    def __call__(self, host):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    safe_ping = SafePing()
    return safe_ping(host)