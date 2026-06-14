from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    if '&&' in input_str or '|' in input_str or ';' in input_str:
        raise ValueError('Invalid characters detected in input')
    return input_str

@app.get("/ping")
def ping(host: str):