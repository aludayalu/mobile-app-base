import litedb,flask,json,re
from flask import Flask,request
app=Flask(__name__)
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
accounts=litedb.get_conn("accounts")

@app.get("/")
def test():
    return ""

def salt_hash(email):
    import hashlib
    return hashlib.sha256(b"saint jhn"+email.encode()+b"roses").hexdigest()

def make_response(data):
    if type(data)!=str:
        data=json.dumps(data)
    resp=flask.Response(data)
    resp.headers["Access-Control-Allow-Origin"]="*"
    resp.headers["Content-Type"]="application/json"
    return resp

@app.get("/auth")
def auth():
    args=dict(request.args)
    if (re.fullmatch(regex,args["email"])):
        pass
    else:
        return make_response({})
    res=accounts.get(args["email"])
    if res in [None,False]:
        accounts.set(args["email"],{"password":salt_hash(args["password"]),"username":args["username"]})
        return make_response({"token":salt_hash(args["email"]),"username":args["username"]})
    elif res["password"]==salt_hash(args["password"]):
        return make_response({"token":salt_hash(args["email"]),"username":res["username"]})
    return make_response({})