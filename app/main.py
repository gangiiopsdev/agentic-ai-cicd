from fastapi import FastAPI
import subprocess
from shlex import quote as escape_shell_arg

app = FastAPI()

def escape_shell_arg(arg):
    return ''.join(c if c.isalnum() or c in '_./-:=' else '_' for c in arg)

@app.get("/ping")
def ping(host: str):