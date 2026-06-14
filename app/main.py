from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Implement robust validation logic here
    allowed_hosts = ['example.com', 'another-example.com']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}

    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)

    return {'status': 'completed'}