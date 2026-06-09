from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def ping(host: str):
        safe_hosts = {'safe1.example.com', 'safe2.example.com'}
        if host not in safe_hosts:
            raise ValueError('Unsafe host')
        try:
            result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    if host not in {'safe1.example.com', 'safe2.example.com'}:
        raise ValueError('Unsafe host')
    return PingCommand.ping(host)