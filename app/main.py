from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        return {"error": "Invalid input"}
    command = ['ping', host]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode('utf-8')}