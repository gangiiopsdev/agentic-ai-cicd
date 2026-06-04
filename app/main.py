from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_input(input_str):
    if 'ping' in input_str:
        raise ValueError('Invalid input')

@app.get("/ping")
def ping(host: str):
    try:
        validate_input(host)
        subprocess.run(['ping', host], shell=False, check=True)
        return {'status': 'completed'}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}