from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        if not self.is_valid_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            result = subprocess.run(['ping', '-c', '1', '--'] + [host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

    def is_valid_host(self, host: str) -> bool:
        # Implement validation logic here (e.g., IP address, domain name format)
        import socket
        try:
            socket.gethostbyname(host)
            return True
        except socket.gaierror:
            return False

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_service = PingService()
    return ping_service.ping(host)