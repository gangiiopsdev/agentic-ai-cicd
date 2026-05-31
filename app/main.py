from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Validate the host input
        if not host.isalnum() or '.' not in host:
            raise ValueError('Invalid host input')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping/{host}')
def ping_endpoint(host: str):
    return SafeSubprocess.ping(host)}