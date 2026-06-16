from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    if not input_string.strip().isalnum():
        raise ValueError("Invalid input")

@app.get("/ping")
def ping(host: str):