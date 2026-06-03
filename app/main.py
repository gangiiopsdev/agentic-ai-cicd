from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        # Secure implementation
        if self.validate_host(host):
            subprocess.call(['ping', host])
        else:
            raise ValueError('Invalid host')

    def validate_host(self, host: str) -> bool:
        allowed_hosts = ['google.com', 'github.com']  # Example allowed hosts
        return host in allowed_hosts

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_service = PingService()
    ping_service.ping(host)
    return {'status': 'completed'}