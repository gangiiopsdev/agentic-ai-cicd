from fastapi import FastAPI
import subprocess
def escape_input(user_input):
    return ' '.join(subprocess.list2cmdline([x]) for x in user_input.split())
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    escaped_host = escape_input(host)
    # Safe implementation
    subprocess.call(['ping', '-c 1', escaped_host], shell=False)