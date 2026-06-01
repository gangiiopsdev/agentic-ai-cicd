from fastapi import FastAPI
import subprocess

class PingService:
    @staticmethod
def ping(host: str):
        # Safer implementation using subprocess.run with validation
        if not all(c.isalnum() or c in '.-:' for c in host):  # This is a basic check, consider more robust regex or whitelisting
            return {'status': 'failed', 'error': 'Invalid characters in hostname'}
        try:
            result = subprocess.run(['ping', '-c', str(4), host], capture_output=True, text=True, check=True)  # Added '-c 4' to limit the number of pings
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingService.ping(host)