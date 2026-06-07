from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(user_input):
    return shlex.quote(user_input)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ['ping', sanitize_input(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}