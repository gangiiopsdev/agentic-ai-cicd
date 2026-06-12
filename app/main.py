from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    subprocess.call(f'ping {escape_shell_argument(host)}', shell=False)

    return {"status": "completed"}