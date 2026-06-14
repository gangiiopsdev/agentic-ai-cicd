from fastapi import FastAPI
class PingService:
    @staticmethod
def ping(host: str):
        if not all(char.isalnum() or char in '._-' for char in host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    service = PingService()
    return service.ping(host)