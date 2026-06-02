from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c in ['-', '.', '_'])
    try:
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
        return {'status': 'completed', 'response': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}