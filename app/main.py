from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    # Add validation logic here
    return host.strip().endswith('.com')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        # Safe implementation
        subprocess.call(['ping', subprocess.quote(host)])
        return {'status': 'completed'}
    else:
        return {'status': 'invalid input'}, 400