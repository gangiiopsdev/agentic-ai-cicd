from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        # Validate the input to ensure it's a valid hostname or IP address
        import ipaddress
        if not (ipaddress.ip_address(host) or host in ['localhost', '127.0.0.1']):
            return {'error': 'Invalid host'}
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': result.stdout}
    except Exception as e:
        return {'error': str(e)}