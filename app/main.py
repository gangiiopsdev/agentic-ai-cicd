from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate and sanitize host input
    if not validate_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

# Example validation function
def validate_host(host: str) -> bool:
    # Add your validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts