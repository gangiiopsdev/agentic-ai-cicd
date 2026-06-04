from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(cmd):
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    cmd = ['ping', host]
    output = execute_command(cmd)

    return {"status": "completed", "output": output}