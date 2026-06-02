from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def validate_host(host: str) -> bool:
        # Basic validation: disallow null bytes and control characters
        return all(c not in host for c in '\x00\x01\x02\x03\x04\x05\x06\x07\x08\x0b\x0c\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f')

app = FastAPI()
def ping(host: str):
    if SafePing.validate_host(host):
        args = ['ping', host]
        subprocess.run(args, check=True)  # Use subprocess.run instead of subprocess.call
    else:
        raise ValueError('Invalid host')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping_fixed(host: str):
    if SafePing.validate_host(host):
        args = ['ping', host]
        subprocess.run(args, check=True)  # Use subprocess.run instead of subprocess.call
    else:
        raise ValueError('Invalid host')
    return {"status": "completed"}