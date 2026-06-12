from fastapi import FastAPI
import subprocess
global_ping = subprocess.Popen(['ping', '{host}'])