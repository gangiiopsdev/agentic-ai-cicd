from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    try:
        # Safe implementation using subprocess.run with shell=False and args parameter
        result = subprocess.run(['ping', host], check=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

def ping(host: str):
    return run_ping(host)