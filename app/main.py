from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Safe implementation using subprocess.run with validation
        host = validate_input(host)
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

def validate_input(input_string: str) -> str:
    # Validate the input to prevent command injection
    if not input_string.isalnum():
        raise ValueError('Invalid input')
    return input_string