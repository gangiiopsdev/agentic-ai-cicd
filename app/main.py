from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str) -> int:
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.returncode
        except subprocess.CalledProcessError as e:
            print(f'Ping failed with error: {e}')
            return 1

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return {'status': SafePing.safe_ping(host)}