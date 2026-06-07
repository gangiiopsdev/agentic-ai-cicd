from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    if not is_safe_hostname(host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return PingService.ping(host)

def is_safe_hostname(hostname: str) -> bool:
    # Implement a function to validate the hostname
    return hostname.isalnum() and '.' in hostname