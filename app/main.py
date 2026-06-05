from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run and avoiding shell=True
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):  # Renaming function to avoid name conflict with the imported function
    return ping(host)