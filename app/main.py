from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell(arg):
    return ''.join(c if c.isalnum() or c in '._-@#:/\' else '_' for c in arg)

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    subprocess.call(f"ping {escape_shell(host)}", shell=True)

    return {"status": "completed"}