from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and executable parameter to avoid command injection.
    try:
        result = subprocess.run(['/bin/ping', host], check=True, capture_output=True, text=True)
        return {'host': host, 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'host': host, 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)