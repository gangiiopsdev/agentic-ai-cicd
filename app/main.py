from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}

@app.get("/ping")
def ping_wrapper():
    return ping('example.com')