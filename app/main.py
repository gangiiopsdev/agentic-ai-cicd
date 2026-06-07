from fastapi import FastAPI
import subprocess
import shlex
def escape_command(input_str):
    return shlex.quote(input_str)
app = FastAPI()
@app.get("/ping")
def ping(host: str):