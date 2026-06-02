from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Validate the host input more strictly to prevent injection
        if not all(c.isalnum() or c in '._' for c in host) or '.' not in host:
            raise ValueError('Invalid host input')
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping/{host}')
def ping_endpoint(host: str):
    # Validate the host input more strictly to prevent injection
    if not all(c.isalnum() or c in '._' for c in host) or '.' not in host:
        raise ValueError('Invalid host input')
    return SafeSubprocess.ping(host)}