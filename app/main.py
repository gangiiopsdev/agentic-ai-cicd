from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/ping")
def ping_safe(host: str):
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except Exception as e:
        return {'status': 'failed', 'error': 'An unexpected error occurred'}