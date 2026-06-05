from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            # Use a whitelist of allowed hosts or IP addresses
            allowed_hosts = ['127.0.0.1', 'localhost']
            if host not in allowed_hosts:
                raise ValueError('Invalid host')
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    # Remove potentially dangerous characters from the input
    sanitized_host = ''.join(c for c in host if c.isalnum() or c.isdigit() or c in ('.', '-', ':'))
    return PingService.ping(sanitized_host)