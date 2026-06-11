from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Basic sanitization, improve as needed
    return ''.join(e for e in input_str if e.isalnum() or e in '-.:')

@app.get("/ping")
def ping(host: str):