from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Validate and sanitize host input
        if not all(c.isalnum() or c in ['.', '-'] for c in host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        command = ['ping', host]
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return SafeSubprocess.ping(host)