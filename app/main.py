from fastapi import FastAPI
import ping3

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/safe-ping')
def safe_ping(host: str):
    # Safe implementation using ping3 library
    try:
        response = ping3.ping(host, timeout=5)
        if response is not None:
            return {'status': 'completed', 'response_time': response}
        else:
            return {'status': 'failed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}