from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Validate input to prevent command injection
        if not host.isalnum():
            return {'status': 'failed', 'error': 'Invalid characters in host name'}
        try:
            result = subprocess.run(['ping', host], check=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    return SafePing.ping(host)