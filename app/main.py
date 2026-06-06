from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return ' '.join(subprocess.list2cmdline(a.split()) for a in arg.split())

app = FastAPI()

@app.get("/ping")
def ping(host: str):