from fastapi import FastAPI
import subprocess
def escape_command(input_str):
    return input_str.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', escape_command(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    return {"status": "completed"}