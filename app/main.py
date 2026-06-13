from fastapi import FastAPI
import subprocess
import shlex
class PingHandler:
    def __init__(self):
        self.app = FastAPI()

    def run_ping(self, host: str):
        if not host.strip():
            raise ValueError('Invalid hostname')
        # Validate and sanitize the input to avoid injection attacks
        valid_hosts = ['127.0.0.1', 'localhost']  # Example validation list
        if host not in valid_hosts:
            raise ValueError('Hostname is not allowed')
        command = ['ping'] + shlex.split(host)
        subprocess.run(command, capture_output=True, text=True)

    @app.get("/ping")
    def ping(self, host: str):
        self.run_ping(host)
        return {"status": "completed"}

# Usage
ping_handler = PingHandler()
ping_handler.app