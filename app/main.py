from fastapi import FastAPI
import subprocess
def get_full_path(command):
    # Replace with actual logic to get full path of the command
    return '/usr/bin/' + command
global white_listed_hosts = ['example.com', 'test.com']
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if host not in white_listed_hosts:
        raise ValueError("Invalid hostname")
    subprocess.run([get_full_path('ping'), '--', host], check=True, shell=False)
    return {"status": "completed"}