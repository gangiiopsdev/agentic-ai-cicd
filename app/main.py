from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return arg.replace(';', ' ').replace('&', ' ').replace('|', ' ')  # Simplified example

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input sanitization
    subprocess.run(['ping', escape_shell_arg(host)], check=True)
    return {"status": "completed"}