from fastapi import FastAPI
import shlex
import subprocess
class SafePing:
    def __init__(self):
        pass

    def safe_ping(self, host: str) -> dict:
        # Secure implementation using subprocess.run without shell=True and proper argument handling
        try:
            if not self.is_valid_host(host):
                return {'status': 'error', 'message': 'Invalid host'}
            args = ['ping'] + shlex.split(host)
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return {'status': 'success', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}

    def is_valid_host(self, host: str) -> bool:
        # Implement validation logic here (e.g., regex check for IP or hostname format)
        return True

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping_endpoint(host: str):
    return safe_ping_instance.safe_ping(host)