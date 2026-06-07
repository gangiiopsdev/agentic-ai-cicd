from fastapi import FastAPI
import subprocess
import re

class SafePing:
    @staticmethod
def ping(host: str):
        # Sanitize input to prevent command injection
        safe_host = re.sub(r'[^a-zA-Z0-9.-_]', '', host)
        try:
            result = subprocess.run(['ping', '-c 1', safe_host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return SafePing.ping(host)