from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        args = ['ping', '-c', '4', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Sanitize input to prevent command injection
    if not host.replace('.', '').isnumeric():
        raise ValueError('Invalid host')
    return ping(host)