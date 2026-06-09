from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return input_string.replace(';', '').replace('&', '').replace('|', '')
given = 'ping ' + sanitize_input(host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.call(given, shell=False)
    return {"status": "completed"}