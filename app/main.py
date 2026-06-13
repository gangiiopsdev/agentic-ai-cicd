from fastapi import FastAPI
import requests
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):  # Use query parameter instead of path parameter
    try:
        validate_host(host)
        response = requests.get(f'http://{host}', timeout=5)
        if response.status_code == 200:
            return {'status': 'completed'}
    except (requests.RequestException, ValueError) as e:
        print(f'Error pinging {host}: {e}')
    return {'status': 'failed'}