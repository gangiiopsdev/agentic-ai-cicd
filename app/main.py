from fastapi import FastAPI
import subprocess

global_vars = globals()
app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)
    return {"status": "completed"}