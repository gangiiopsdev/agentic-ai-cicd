from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
    def ping(host: str):
        try:
            output = subprocess.run(['/usr/bin/ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    safe_ping = SafePing()
    # Use a whitelist approach to allow only known-safe hosts
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host is not allowed'}
    return safe_ping.ping(host)