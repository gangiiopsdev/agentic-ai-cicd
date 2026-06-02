from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.run(['ping', host], timeout=5, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_handler(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    return SafePing.ping(host)

def is_safe_host(host: str) -> bool:
    # Implement logic to validate the host input, e.g., allow only known hosts
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts