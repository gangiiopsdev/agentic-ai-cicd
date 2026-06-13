from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Replace shell=True with a list of arguments
        subprocess.call(['ping', host])
        return True
    except Exception as e:
        print(f'Error pinging {host}: {e}')
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}