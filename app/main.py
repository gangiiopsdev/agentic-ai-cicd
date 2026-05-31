from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def get_full_command(command_parts):
    return ' '.join(shlex.quote(arg) for arg in command_parts)

@app.get("/ping")
def ping(host: str):
    full_command = get_full_command(['ping', host])
    result = subprocess.run(full_command, shell=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}