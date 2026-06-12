from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_arg(arg):
    return ''.join(c if c.isalnum() else '_' for c in arg)

@app.get("/ping")
def ping(host: str):
    escaped_host = shlex.quote(escape_shell_arg(host))
    result = subprocess.run(['ping', escaped_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}