from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell(input_str):
    return input_str.replace(';', '').replace('&', '').replace('|', '').replace('$', '').replace(``, '').replace('`', '')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using check_output and splitting the command into a list
    host = escape_shell(host)
    subprocess.check_output(['ping', f'echo {host}'], stderr=subprocess.STDOUT, shell=False)
    return {"status": "completed"}