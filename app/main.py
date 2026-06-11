from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def safe_ping(host: str):
        try:
            # Validate and sanitize input
            if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', host):
                raise ValueError('Invalid host format')
            subprocess.run(['ping', host], check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': str(e)}

import re
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingService.safe_ping(host)