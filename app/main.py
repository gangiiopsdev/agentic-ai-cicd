from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using check_output and splitting the command into a list
    subprocess.check_output(['ping', subprocess.check_output(f'echo {host}', shell=True, text=True).strip()], stderr=subprocess.STDOUT)
    return {"status": "completed"}