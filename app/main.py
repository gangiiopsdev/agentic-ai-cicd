from fastapi import FastAPI
import subprocess
def secure_ping(host):
    # Secure implementation
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input before passing it to the function
    if not host.isalnum() or '..' in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    return secure_ping(host)