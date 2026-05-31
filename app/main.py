from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', subprocess.check_output(f'echo {host}', shell=True, text=True).strip()], capture_output=True, text=True)

@app.get("/ping")
def ping_route(host: str):
    result = ping(host)
    return {'status': 'completed', 'output': result.stdout}