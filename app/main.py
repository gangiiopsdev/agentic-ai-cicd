from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the input to ensure it is safe
        if not all(char.isalnum() or char in '.-' for char in host):
            raise ValueError('Invalid characters in host parameter')
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}