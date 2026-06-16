from fastapi import FastAPI
import ping3

app = FastAPI()

def is_valid_host(host):
    # Basic validation for simplicity; use more robust methods in production
    return host.replace('.', '').isalnum() and len(host) <= 64

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/safe-ping')
def safe_ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host format'}
    try:
        response = ping3.ping(host, timeout=5)
        if response is not None:
            return {'status': 'completed', 'response_time': response}
        else:
            return {'status': 'failed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}