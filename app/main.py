from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Input validation to allow only alphanumeric and hyphens
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        return {'status': 'failed', 'error': 'Invalid input'}

    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Preventive controls
- Validate the input `host` to ensure it only contains allowed characters (e.g., alphanumeric and hyphens).
- Use a whitelist of allowed host names or IP addresses.
- Log all subprocess executions for monitoring and auditing purposes.