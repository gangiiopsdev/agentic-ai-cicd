from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.Popen
    process = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'status': 'completed'}