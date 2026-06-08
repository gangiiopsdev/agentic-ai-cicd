from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_command(command):
    return ' '.join(map(subprocess.quote, command.split()))

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    result = subprocess.run(escape_shell_command(f"ping {host}").split(), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}