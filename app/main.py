from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        args = ['ping', host]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr.decode("utf-8")}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return safe_ping(host)