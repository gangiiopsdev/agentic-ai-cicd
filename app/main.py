from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.strip() and not any(char in ' 	
\'"`<>;|&*?^()%$#@!~{[}]' for char in host):
        subprocess.run(['ping', host], check=True)
    return {"status": "completed"}