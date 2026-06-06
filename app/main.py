from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    if not all(c.isalnum() or c in '.-' for c in host):
        return {"error": "Invalid hostname"}, 400
    return ping(host)