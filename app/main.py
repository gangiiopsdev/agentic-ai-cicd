from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

@app.get="/ping")
def ping_route(host: str):  # Renamed function to avoid naming conflict with the ping function
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}