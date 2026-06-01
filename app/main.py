from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if host.strip().isdigit():
        args = ['ping', '-c', '4', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'output': result.stdout}
    else:
        return {'error': 'Invalid input'}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)