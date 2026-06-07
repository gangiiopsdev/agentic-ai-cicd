from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate host input to prevent command injection
        if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except (subprocess.CalledProcessError, ValueError) as e:
        return f'Error: {e.output}'

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}