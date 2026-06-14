from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        # Validate host input to prevent injection attacks
        if not validate_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
def validate_host(host: str):
    # Implement a simple validation logic
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)