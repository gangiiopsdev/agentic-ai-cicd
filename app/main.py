from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    return execute_ping(host)

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
    return host in allowed_hosts