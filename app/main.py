from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell(input_string):
    return shlex.quote(input_string)

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote to escape shell characters
    subprocess.call(['ping', escape_shell(host)])
    return {"status": "completed"}