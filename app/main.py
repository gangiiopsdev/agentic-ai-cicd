from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], timeout=5, shell=False)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not SafeSubprocess.is_valid_host(host):
        return {'error': 'Invalid host'}
    return {"status": SafeSubprocess.safe_ping(host)}
class SafeSubprocess:
    @staticmethod
def is_valid_host(host: str) -> bool:
        # Basic validation, more comprehensive checks can be added
        return all(c.isalnum() or c in ['.', '-', '_'] for c in host)