from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    subprocess.call(['ping', escape_shell_argument(host)])

    return {"status": "completed"}