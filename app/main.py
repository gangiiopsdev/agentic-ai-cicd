from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        # Validate input to ensure it does not contain malicious content
        if not host.strip() or not host.isalnum():
            raise ValueError('Invalid host provided')
        command = ['ping', '-c', '1', host]  # Limit the number of pings and use a safe option
        result = subprocess.run(command, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_service = PingService()
    return ping_service.ping(host)