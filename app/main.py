from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Sanitize the host input to prevent injection attacks
        result = subprocess.run(['ping', f'"{host}"'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    # Ensure the host input is sanitized before passing it to subprocess
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    return ping(host)