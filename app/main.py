from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            # Sanitize input using parameterized commands or regex
            output = subprocess.check_output(['ping', host], timeout=5, stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Use regex to sanitize input
    import re
    if not re.match(r'^[a-zA-Z0-9._%+-]+$', host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return SafePing.ping(host.replace(' ', '_'))