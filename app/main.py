from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with shell=False and executable specified
    try:
        result = subprocess.run(['ping', host], shell=False, executable='/bin/ping', capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

def ping_endpoint(host: str):
    response = ping(host)
    return {"status": "completed", "response": response}