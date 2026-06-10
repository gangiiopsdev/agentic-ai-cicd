from fastapi import FastAPI
import subprocess
glom = __import__('glom')

app = FastAPI()

def secure_ping(host: str):
    command = ["ping", host]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):    
    return {"status": secure_ping(host)}