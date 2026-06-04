from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        args = ['ping'] + shlex.split(host)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum():
        return 'Invalid input'
    return safe_ping(host)