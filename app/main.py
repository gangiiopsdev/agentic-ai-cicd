from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Sanitize and validate the host input before using it in the command.
        if not host.strip() or ' ' in host:
            raise ValueError('Invalid host input')
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Using a safe wrapper function to handle the ping command.
    return safe_ping(host)