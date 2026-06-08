from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Use a whitelist of allowed hosts or IP ranges
        if host not in ['example.com', '192.168.1.1']:
            raise ValueError('Invalid host')
        args = ['ping', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Safer implementation with a whitelist of allowed hosts
    return safe_ping(host)