from flask import Flask
app = Flask(__name__)

@app.route('/convert')
def convert():
  # code to convert YouTube video  
  return 'result.mp4'
python python_converter.py
