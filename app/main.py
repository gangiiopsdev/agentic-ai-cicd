from fastapi import FastAPI
import shlex
import subprocess
import re
class SafePing:
    @staticmethod
def ping(host: str) -> dict:
        # Validate the host input to ensure it is an IP address
        if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', host):
            return {'status': 'error', 'message': 'Invalid IP address format'}
        # Sanitize the host input to prevent shell injection
        safe_host = shlex.quote(host)
        args = ['ping', '-c', '4', safe_host]  # Limiting the number of pings for security
        try:
            result = subprocess.run(args, capture_output=True, text=True, check=True, timeout=10)  # Adding a timeout
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}
        except subprocess.TimeoutExpired:
            return {'status': 'error', 'message': 'Command timed out'}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str) -> dict:
    return SafePing.ping(host)