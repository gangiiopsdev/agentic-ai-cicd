from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Preventive controls
1. Validate and sanitize user input for the 'host' parameter.
2. Use a whitelist of allowed host values.
3. Avoid using subprocess if possible, consider using other libraries like ping3.