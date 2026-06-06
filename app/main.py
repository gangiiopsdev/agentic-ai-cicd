from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

def escape_shell_arg(arg):
    return ' '.join(shlex.quote(c) for c in arg.split())

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.Popen
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}