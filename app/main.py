from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error pinging {host}: {e.stderr}'
    except Exception as e:
        return f'An unexpected error occurred: {e}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host or not isinstance(host, str) or ' ' in host:
        return {'status': 'Invalid input'}
    # Sanitize the host input before using it in the command
    sanitized_host = ''.join(c for c in host if c.isalnum() or c.isdigit() or c in [ '.', '-', '_' ])
    return {'status': safe_ping(sanitized_host)}