from fastapi import FastAPI
import ping3
from urllib.parse import quote
global host_whitelist = set(['example.com', 'test.com'])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in host_whitelist:
        return {'error': 'Host is not allowed'}
    try:
        response = ping3.ping(host, timeout=1)
        if response is None:
            return {'error': 'Ping failed'}
    except Exception as e:
        return {'error': str(e)}
    return {'status': 'completed'}