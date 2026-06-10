from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Validate and sanitize the host input
        if not validate_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        output = subprocess.check_output(['ping', host], shell=False, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

# Helper function to validate host input
def validate_host(host):
    # Add your validation logic here, e.g., regex matching against allowed IP addresses or domain names
    import re
    pattern = r'^[0-9]{1,3}\.[0-9]{1,3}\.\[0-9]{1,3}\.\[0-9]{1,3}$'
    return re.match(pattern, host) is not None