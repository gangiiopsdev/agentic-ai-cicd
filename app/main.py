from fastapi import FastAPI
import subprocess
global host_list
host_list = ['google.com', 'example.com']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in host_list:
        return {'error': 'Host not allowed'}
    # Secure implementation using subprocess.run with shell=False
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
    return {'status': 'completed'}