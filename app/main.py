from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            # Use a whitelist of allowed hosts or validate input
            if host in ['allowed_host1', 'allowed_host2']:
                subprocess.run(['ping', host], check=True, shell=False)
                return 'Ping successful'
            else:
                raise ValueError('Invalid host')
        except subprocess.CalledProcessError as e:
            return f'Ping failed with error {e.returncode}

app = FastAPI()
def ping_route(host: str):
    service = PingService()
    return service.ping(host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}