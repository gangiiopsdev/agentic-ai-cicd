from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg: str) -> str:
    return arg.replace(';', '').replace('&', '')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input sanitization
    try:
        safe_host = escape_shell_arg(host)
        output = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}