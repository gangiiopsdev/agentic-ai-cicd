from fastapi import FastAPI
import subprocess
class SafePinger:
    def __init__(self):
        pass

    @staticmethod
def safe_ping(host: str) -> str:
        # Validate input more robustly
        if not host.isalnum():
            return "Invalid input"
        # Use a whitelist of allowed hosts or IP ranges
        allowed_hosts = ['example.com', '192.168.1.1']
        if host not in allowed_hosts:
            return "Host not allowed"
        cmd = ['ping', host]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e.stderr)

app = FastAPI()
pinger = SafePinger()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = pinger.safe_ping(host)
    return {'status': 'completed', 'result': result}