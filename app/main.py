from fastapi import FastAPI
import subprocess
from fastapi.params import Query

app = FastAPI()

@app.get("/ping")
def ping(host: str = Query(..., min_length=1, max_length=255)):
    try:
        # Validate and sanitize the input
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}