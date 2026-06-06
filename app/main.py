from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))

@app.get("/ping")
def ping(host: str):