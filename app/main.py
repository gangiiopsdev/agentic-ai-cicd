from fastapi import FastAPI
import subprocess
class SafePing:
    def ping(self, host: str):
        # Secure implementation using subprocess.run
        try:
            result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_ping = SafePing()
    return safe_ping.ping(host)