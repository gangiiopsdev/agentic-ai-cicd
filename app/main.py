from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    try:
        return shlex.quote(input_str)
    except Exception as e:
        raise ValueError(f'Invalid input: {e}')

@app.get("/ping")
def ping(host: str):