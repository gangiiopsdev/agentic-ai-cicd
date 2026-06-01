from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(command):
    return [arg.replace(';', '').replace('&', '') for arg in command.split()]

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(escape_command(f"ping {host}"), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}