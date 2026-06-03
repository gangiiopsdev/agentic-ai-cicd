from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            # Using subprocess.run instead of subprocess.call for better control and safety.
            result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    # Use a whitelist of allowed hosts or use a library designed for safe subprocess execution
    if host not in ['example.com', 'localhost']:
        return {'status': 'failed', 'error': 'Host not allowed'}
    return SafePing.ping(host)