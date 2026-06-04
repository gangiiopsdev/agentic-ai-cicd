from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return ''.join(c if c.isalnum() or c in '_.-@:/\,=' else '\' + c for c in arg)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(f'ping {escape_shell_arg(host)}', shell=True)
    return {"status": "completed"}