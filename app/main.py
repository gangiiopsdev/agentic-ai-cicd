from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return ' '.join(quote(a) for a in arg.split())

app = FastAPI()

@app.get("/ping")
def ping(host: str):