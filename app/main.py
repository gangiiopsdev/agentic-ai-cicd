from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

def ping(host: str):
    # Fixed implementation using a list for the command arguments and shell=False
    try:
        subprocess.run(['ping'] + shlex.split(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    else:
        return {'status': 'completed'}