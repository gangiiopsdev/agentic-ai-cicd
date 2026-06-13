from fastapi import FastAPI
import re

class SafePing:
    @staticmethod
def ping(host: str):
        # Regular expression to validate host input
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'failed', 'error': 'Invalid host'}
        safe_host = subprocess.quote(host)
        try:
            result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return SafePing.ping(host)