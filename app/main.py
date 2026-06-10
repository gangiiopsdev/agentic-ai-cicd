from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command, *args):
    return subprocess.run(command, args=args, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    result = run_command(['ping', host])
    return {'status': 'completed', 'output': result.stdout}