from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate host input
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True, shell=False)
        print(f'Ping successful: {result.stdout}')
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')

app = FastAPI()

@app.get('/ping/{host}')
def ping_endpoint(host: str):
    return {'message': 'Ping request processed'}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts