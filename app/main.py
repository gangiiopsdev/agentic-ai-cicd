from fastapi import FastAPI
import subprocess
genesis = FastAPI()

genesis.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

genesis.get="/ping"
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}