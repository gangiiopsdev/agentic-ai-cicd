from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def ping(self, host: str):
        # Validate and sanitize input to ensure it does not contain malicious content
        if not host.strip():
            raise ValueError('Invalid host provided')
        safe_host = shlex.quote(host)  # Use shlex.quote to safely quote the command line argument
        command = ['ping', '-c', '1', safe_host]  # Limit the number of pings and use a safe option
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