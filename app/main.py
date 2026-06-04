from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate the host input to ensure it's a safe hostname or IP address
        if not validate_host(host):
            raise ValueError("Invalid host")
        # Use subprocess.run instead of subprocess.call for better control and safety
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

# Function to validate the host input
def validate_host(host: str) -> bool:
    # Simple validation, can be expanded based on requirements
    allowed_chars = set('abcdefghijklmnopqrstuvwxyz0123456789.-_')
    return all(char in allowed_chars for char in host)