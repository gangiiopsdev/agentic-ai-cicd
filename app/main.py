from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    if not input_string.strip().isalnum():
        raise ValueError("Invalid input")

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(["ping", host], check=True, stdout=subprocess.PIPE)
        return {"result": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr.decode()}