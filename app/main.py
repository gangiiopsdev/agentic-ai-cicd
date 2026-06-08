from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Constructing the command without using shell=True for security
        args = ['ping', host]
        if 'localhost' not in host and '127.0.0.1' not in host:
            return {'status': 'failed', 'error': 'Untrusted input detected'}
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)