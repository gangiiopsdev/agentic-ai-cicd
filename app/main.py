from fastapi import FastAPI
import subprocess
generics = ['192.168.0.1', '8.8.8.8'] # Allowed hosts list

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in generics:
        try:
            subprocess.run(['ping', '-c', '4', host], check=True, shell=False)
        except subprocess.CalledProcessError as e:
            return {'status': 'Failed to ping', 'error': str(e)}
    else:
        return {'status': 'Invalid host'}
    return {'status': 'completed'}