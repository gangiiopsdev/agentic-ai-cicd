from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return ' '.join(subprocess.list2cmdline([arg]) for arg in args)

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}