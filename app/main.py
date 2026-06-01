from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f'Error pinging {host}: {e.stderr}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}