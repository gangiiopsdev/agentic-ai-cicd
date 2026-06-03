from fastapi import FastAPI
import subprocess
import re

def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9]{1,255}$', host) is not None

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}

    # Use the ping3 library for safer and more secure handling of pings
    try:
        import ping3
        response = ping3.ping(host)
        if response is not None:
            return {'status': 'completed', 'output': f'Ping to {host} successful. Time: {response} ms'}
        else:
            return {'status': 'error', 'message': 'Ping failed'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}