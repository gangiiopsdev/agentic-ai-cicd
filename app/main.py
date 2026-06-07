from fastapi import FastAPI
import subprocess
import shlex
class SafePinger:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    async def ping(self, host: str):
        # Validate the host input to ensure it does not contain malicious content
        if not self.is_valid_host(host):
            return {'status': 'error', 'message': 'Invalid host'}
        command = ['ping', host]
        result = subprocess.run(command, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

    def is_valid_host(self, host):
        # Implement validation logic here, e.g., using a whitelist or regex
        allowed_hosts = ['example.com', 'localhost']
        return host in allowed_hosts}