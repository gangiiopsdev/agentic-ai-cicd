from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use the ping3 library for safe ping operations instead of subprocess
        from ping3 import ping, verbose_ping
        response = verbose_ping(host)
        if response is not None:
            return f'Ping to {host} successful. Time: {response}s'
        else:
            return f'Ping to {host} failed.'
    except Exception as e:
        return f'An error occurred: {str(e)}'

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)