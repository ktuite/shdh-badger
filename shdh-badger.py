from flask import Flask, render_template, request, jsonify
from subprocess import Popen
from tempfile import TemporaryFile
from base64 import b64decode

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('signin.html')

@app.route("/print", methods=['POST'])
def print_badge():
  filedata = b64decode(request.form['image'].replace("data:image/png;base64,", ""))

  #with open("last.png", "wb") as f:
  #  f.write(filedata)

  f = TemporaryFile(mode='w+b')
  f.write(filedata)
  f.seek(0)
  proc = Popen("lpr", shell=True, stdin=f)
  proc.wait()
  return str(proc.returncode)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
