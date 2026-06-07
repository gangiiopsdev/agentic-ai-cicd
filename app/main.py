from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command, *args):
    subprocess.run([command] + list(args), check=True)

@app.get("/ping")
def ping(host: str):
    execute_safe_command('ping', host)
    return {"status": "completed"}