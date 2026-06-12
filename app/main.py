from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Secure implementation using a whitelist of allowed hosts or IPs
        allowed_hosts = ['127.0.0.1', '::1']
        if host in allowed_hosts:
            subprocess.call(['ping', host])
            return {'status': 'completed'}
        else:
            return {'error': 'Unauthorized access'}, 403

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    return SafePing.ping(host)