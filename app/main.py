from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        allowed_hosts = ['example.com', 'another-example.com']
        if host in allowed_hosts:
            args = ['ping', host]
            subprocess.call(args)
            return {"status": "completed"}
        else:
            return {"error": "Host not allowed"}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return SafePing.ping(host)