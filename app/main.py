from fastapi import FastAPI
import subprocess
def execute_safe_command(command, *args):
    sanitized_args = [arg.strip() for arg in args]
    subprocess.run([command] + list(sanitized_args), check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    execute_safe_command('ping', host.strip())
    return {"status": "completed"}