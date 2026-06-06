from fastapi import FastAPI
import subprocess

class SafeSubprocess:
    @staticmethod
def safe_subprocess(command: list):
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Command failed with error: {e.stderr}'

app = FastAPI()

def ping(host: str):
    if not host or len(host) > 255 or '"' in host or ';' in host or '&' in host:
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    return SafeSubprocess.safe_subprocess(args)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)