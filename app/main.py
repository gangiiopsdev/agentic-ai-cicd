from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

# Define a function to validate the host input
def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., check if the host matches expected patterns
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None}