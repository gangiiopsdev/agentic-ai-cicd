from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Validate and sanitize the host input
        if not is_valid_host(host):
            raise ValueError("Invalid host")
        args = ['ping', host]
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
def is_valid_host(host: str):
    # Implement validation logic here
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts
app = FastAPI()
@app.get("/ping")
def ping(host: str):    return safe_ping(host)