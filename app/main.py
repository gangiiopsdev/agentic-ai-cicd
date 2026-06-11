from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return ''.join(c if c.isalnum() else '_' for c in arg)

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    subprocess.call(['ping', escape_shell_arg(host)])

    return {"status": "completed"}