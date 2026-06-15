from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate the host input to prevent injection attacks
        if not validate_hostname(host):
            raise ValueError("Invalid hostname")
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

def validate_hostname(hostname: str) -> bool:
    # Implement a more robust validation logic here, e.g., regex
    import re
    pattern = re.compile(r'^[a-zA-Z0-9-.]+$')
    return bool(pattern.match(hostname))