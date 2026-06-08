from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return ''.join(c if c.isalnum() or c in '_./-:=' else '_' for c in arg)

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    subprocess.call(['ping', escape_shell_arg(host)])

    return {"status": "completed"}