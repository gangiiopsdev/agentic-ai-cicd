from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum() or '.' in host:
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'success', 'message': 'Host is valid'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result['status'] == 'error':
        return result
    subprocess.call(['ping', host])  # This line can still be risky, but the validation helps mitigate risks
    return {'status': 'completed'}