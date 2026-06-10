from fastapi import FastAPI
import requests
def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '.-')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise ValueError("Invalid input")

    try:
        response = requests.get(f"http://{sanitized_host}", timeout=5)  # Added timeout
        return {'status': 'completed', 'stdout': response.text, 'stderr': ''}
    except Exception as e:
        return {'status': 'failed', 'stdout': '', 'stderr': str(e)}