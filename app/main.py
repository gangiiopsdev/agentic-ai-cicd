from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_input(user_input):
    # Simple escaping, real-world use should be more robust
    return ''.join(c if c.isalnum() else '_' for c in user_input)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_input(host)
    subprocess.run(shlex.split(f'ping {escaped_host}'), check=True)
    return {"status": "completed"}