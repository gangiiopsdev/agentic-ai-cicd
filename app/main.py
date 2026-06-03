from fastapi import FastAPI
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum() or not os.path.exists(host):
        return {'error': 'Invalid host'}
    subprocess.run(['ping', f'{host}'], check=True, shell=False)
    return {'status': 'completed'}