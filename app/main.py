from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Secure implementation using subprocess.run with args parameter
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f'Ping failed: {e.stderr.strip()}')
            return False
class PingEndpoint:
    def __init__(self):
        self.app = FastAPI()
    @app.get("/ping")
def ping_endpoint(host: str):
        # Validate input to prevent command injection
        if not host.replace('.', '').isnumeric():
            return {"status": "failed", "reason": "Invalid input"}
        result = SafeSubprocess.ping(host)
        if result:
            return {"status": "completed"}
        else:
            return {"status": "failed"}