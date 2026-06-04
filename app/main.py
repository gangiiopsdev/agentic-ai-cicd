from fastapi import FastAPI
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9]{1,64}$', host):
        raise ValueError('Invalid input')
    result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}