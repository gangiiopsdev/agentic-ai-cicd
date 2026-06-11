from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use ping3 for safer and more secure ping operations
    try:
        from ping3 import ping
        response_time = ping(host, timeout=2)
        if response_time is not None:
            return {'status': 'completed', 'response_time': response_time}
        else:
            return {'status': 'unreachable'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)