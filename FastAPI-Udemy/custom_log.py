from fastapi import Request

def log(tags="My-Response-API",message="No Message",request:Request=None):
    with open("log.txt","a+") as f:
        f.write(f"{tags} : {message} \n")
        f.write(f"{request.url} \n ")
        
def database_log(tags="My-DB1-API",message="No Message",request:Request=None):
    with open("db_log.txt","a+") as f:
        f.write(f"{tags} : {message} \n")
        f.write(f"{request.url} \n ")