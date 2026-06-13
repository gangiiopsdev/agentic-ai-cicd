from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            # Use a whitelist of allowed hosts
            allowed_hosts = ['example.com', 'google.com']
            if host not in allowed_hosts:
                return {'status': 'failed', 'error': 'Host not allowed'}
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'result': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingService.ping(host)