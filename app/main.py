from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    # Simple validation example - real-world use might require more sophisticated checks
    return all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host)

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.call(["ping", host])
    else:
        raise ValueError('Invalid hostname')
    
    return {"status": "completed"}