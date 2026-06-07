from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    # Simple input sanitization
    return ''.join(c for c in user_input if c.isalnum() or c in (',', '.', ' ', '-'))

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}