from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        return ping(host)
    except Exception as e:
        return {'error': str(e)}