from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Use a whitelist for allowed hosts or implement proper validation
        allowed_hosts = ['example.com', 'test.com']  # Replace with actual list of allowed hosts
        if host not in allowed_hosts:
            return {'error': 'Invalid input'}
        command = ['ping', shlex.quote(host)]  # Use shlex.quote to safely quote the host
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    return SafeSubprocess.ping(host)