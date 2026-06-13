from fastapi import FastAPI
import subprocess
import re
class PingService:
    @staticmethod
def safe_ping(host: str):
        try:
            # Validate and sanitize input
            if not re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\.\.[0-9]{1,3}\.\.[0-9]{1,3}$', host) or len(host.split('.')) != 4:
                raise ValueError('Invalid host format')
            subprocess.run(['ping', '-c', '1', host], check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': str(e)}

import re
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingService.safe_ping(host)