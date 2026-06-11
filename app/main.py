from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    def ping(self, host: str):
        if not host or not host.strip().isalnum():
            raise ValueError('Invalid host')
        # Using shlex to safely handle command arguments
        command = shlex.split(f'ping {host}')
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping_service.ping(host)