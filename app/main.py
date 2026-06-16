from fastapi import FastAPI
import paramiko

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username='user', password='password')
    stdin, stdout, stderr = client.exec_command('ping 127.0.0.1')
    output = stdout.read().decode()
    return {"status": "completed", "output": output}