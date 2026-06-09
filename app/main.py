from fastapi import FastAPI
import subprocess
global app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input
        if not host.isalnum():
            raise ValueError('Invalid host input')
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    except ValueError as e:
        return {'error': str(e)}