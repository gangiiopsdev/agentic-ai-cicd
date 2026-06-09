from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Use a whitelist for allowed hosts or implement proper validation
        if not host.isalnum():
            return {'error': 'Invalid input'}
        command = ['ping', host]
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    if not any(char.isalnum() for char in host):
        return {'error': 'Invalid input'}
    return SafeSubprocess.ping(host)