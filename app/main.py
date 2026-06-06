from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
    def ping(host: str):
        try:
            output = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
            return {'status': 'completed', 'output': output.stdout.decode('utf-8')}
        except subprocess.TimeoutExpired as e:
            return {'status': 'failed', 'error': f'Ping timed out: {e}'}}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    result = SafeSubprocess.ping(host)
    return result