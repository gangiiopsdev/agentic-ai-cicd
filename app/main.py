from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return ''.join(c if c.isalnum() or c in '_.-@:/\,=' else '\' + c for c in arg)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    subprocess.run(['ping', escape_shell_arg(host)], check=True)
    return {"status": "completed"}