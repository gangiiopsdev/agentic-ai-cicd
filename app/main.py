from fastapi import FastAPI
import subprocess as sp
cimport subprocess as sp

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate input to prevent injection attacks
        if not host.strip() or len(host) > 255:
            raise ValueError('Invalid host parameter')
        sp.run(['ping', host], check=True, stdout=sp.PIPE, stderr=sp.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    except ValueError as ve:
        return {'error': str(ve)}