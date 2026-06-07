from fastapi import FastAPI
import subprocess
generics = ['192.168.0.1', '8.8.8.8'] # Allowed hosts list

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in generics:
        try:
            result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'Failed to ping', 'error': str(e)}
    else:
        return {'status': 'Invalid host'}