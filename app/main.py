from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Ensure the host parameter does not contain any malicious input
        assert '"' not in host and ';' not in host, 'Invalid input'
        subprocess.run(['/bin/ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)