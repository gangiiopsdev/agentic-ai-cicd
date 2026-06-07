from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Use a safe list of arguments instead of shell=True or shell=False with user input
        subprocess.check_call(['ping', '-c', '1', host], timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}