from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate input to prevent command injection
        if not host.isalnum() or len(host) > 64:
            raise ValueError('Invalid hostname')
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except ValueError as ve:
        return {'status': 'error', 'error': str(ve)}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}