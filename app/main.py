from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the input to prevent injection attacks
        safe_host = host.strip()
        if safe_host.isalnum():
            result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'failed', 'error': 'Invalid input'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}