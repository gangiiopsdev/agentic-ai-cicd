from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True, shell=False)
        print(f'Ping successful: {result.stdout}')
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')

app = FastAPI()

@app.get('/ping/{host}')
def ping_endpoint(host: str):
    return {'message': 'Ping request processed'}