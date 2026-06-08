from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Splitting the command into an array to avoid shell injection
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)