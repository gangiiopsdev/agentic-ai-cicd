from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_user_input(user_input):
    return user_input.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_user_input(host)
    try:
        subprocess.call(['ping', safe_host], shell=False)
    except Exception as e:
        return {'error': str(e)}

    return {'status': 'completed'}