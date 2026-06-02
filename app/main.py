from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        return None, 'Invalid input'
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout, None

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Basic validation to prevent command injection
    output, error_message = safe_ping(host)
    if error_message:
        return {'status': 'error', 'message': error_message}
    return {'status': 'completed', 'output': output}