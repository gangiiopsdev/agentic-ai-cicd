from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error pinging {host}: {e.stderr}'
    except Exception as e:
        return f'An unexpected error occurred: {e}\nUnauthorized command execution attempted. Please provide a valid host.'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host or not isinstance(host, str) or ' ' in host:
        return {'status': 'Invalid input'}
    return {'status': safe_ping(host)}