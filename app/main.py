from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(args, **kwargs):
        try:
            return subprocess.run(args, check=True, **kwargs)
        except subprocess.CalledProcessError as e:
            raise ValueError(f'Command failed with error: {e}')

app = FastAPI()

def is_safe_host(host):
    # Implement a whitelist of allowed hosts
    return host in ['safehost1', 'safehost2']

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        args = ['ping', host]
        SafeSubprocess.run(args)
    else:
        raise ValueError('Host not allowed')

    return {"status": "completed"}