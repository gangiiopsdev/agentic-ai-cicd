from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/ping/{host}")
def ping(host: str):
    try:
        # Validate host input to prevent command injection
        if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        response = requests.get(f"http://{host}", timeout=1)
        return {'status': 'completed', 'output': response.status_code}
    except requests.exceptions.RequestException as e:
        return {'status': 'failed', 'error': str(e)}