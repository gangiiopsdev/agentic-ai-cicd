from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str) -> dict:
        try:
            # Validate the host input
            if not host.strip() or not host.isalnum():
                return {'status': 'failed', 'error': 'Invalid hostname'}
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return SafePing.safe_ping(subprocess.check_output(['hostname'], text=True).strip())