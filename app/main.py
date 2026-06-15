from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 20:
        return {'status': 'error', 'message': 'Invalid input'}
    # Use a safe alternative for pinging, e.g., using ping3 library
    try:
        import ping3
        response = ping3.ping(host)
        if response is not None:
            return {'status': 'completed', 'response_time': response}
        else:
            return {'status': 'error', 'message': 'Ping failed'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}