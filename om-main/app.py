from flask import Flask
app = Flask("__om__")
@app.route('/')
def home():
    return "habibi welcome to cloud"
if __name__=='__main__':
    app.run()
    