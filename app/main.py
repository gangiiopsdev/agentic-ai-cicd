from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            # Use a whitelist of allowed hosts and avoid passing user input directly to the command line
            if not is_safe_host(host):
                raise ValueError('Invalid host')
            output = subprocess.run(['ping', host], timeout=5, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_handler(host: str):
    try:
        # Validate the host input, e.g., allow only known hosts
        if not is_safe_host(host):
            raise ValueError('Invalid host')
        return SafePing.ping(host)
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}
def is_safe_host(host: str) -> bool:
    # Implement logic to validate the host input, e.g., allow only known hosts
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts