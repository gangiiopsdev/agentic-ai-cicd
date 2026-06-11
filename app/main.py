from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e), 'stderr': e.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    # Validate the host input to ensure it is a safe hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Simple regex for demonstration purposes
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return SafePing.ping(host)