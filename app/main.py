from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(arg):
    return arg.replace('`', '\\').replace('$', '\\$')

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.Popen
    escaped_host = escape_shell_argument(host)
    args = ['ping', escaped_host]
    subprocess.run(args, check=True)
    return {"status": "completed"}