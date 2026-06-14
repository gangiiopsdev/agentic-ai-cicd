from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> None:
    if not host.startswith('127.0.0.1') and not host.startswith('localhost'):
        raise ValueError("Host must be either '127.0.0.1' or 'localhost'")
    try:
        args = ['ping', host]
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        print(f'Error pinging {host}: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}