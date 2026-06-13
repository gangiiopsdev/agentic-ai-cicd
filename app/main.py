from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with proper error handling
    try:
        # Validate and sanitize host input
        if not is_valid_host(host):
            raise ValueError("Invalid host")
        result = subprocess.run(shlex.split('ping ' + host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

def is_valid_host(host: str) -> bool:
    # Add your validation logic here, e.g., regex to match allowed host patterns
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None