from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_input(input_str):
    return input_str.replace(';', ' ').replace('&', ' ').replace('|', ' ').replace('*', ' ').replace('(', '').replace(')', '')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(f'ping {escape_shell_input(host)}', shell=False)
    return {"status": "completed"}