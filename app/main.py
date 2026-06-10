from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.isnumeric() and 1 <= int(host) <= 254:
        args = ['ping', f'192.168.0.{host}']
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host input"}