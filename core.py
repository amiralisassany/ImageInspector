from PIL import Image, ImageFilter, ImageEnhance
import io
from utils import utl
import base64

import os,sys
sys.path.append(os.path.abspath("plugins/"))
plugins = list(map(lambda x: x.replace(".py", ""), os.listdir('plugins/')))


class Process:
    def export(self, format="png"):
        self.file = io.BytesIO()
        img = self.main.raw
        img.save(self.file, format=format)
        return self.file

    def show(self):
        return self.main.raw.show()

class Handler(Process):
    def __init__(self, pname, img, args={}):
        if args == {}: 
            self.main = __import__(pname).Main(img)
        else : 
            self.main = __import__(pname).Main(img,args)

# API
 
from flask import Flask, request, send_file, jsonify
import json

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    data_field = request.form.get('data')

    if not file or not data_field:
        return jsonify({'error': 'Missing file or data field'}), 400

    try:
        data = json.loads(data_field)
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON in data field'}), 400
    if not data["plugin"].replace('.py','') in plugins:
        return "Plugin does not exist."
 
    img = Image.open(file.stream)
    handler = Handler(data['plugin'],img,data['args'])
    output = handler.export()
    output.seek(0)
    
    output_content = output.read()

    return send_file(
        io.BytesIO(output_content),
        mimetype='image/png',
        as_attachment=True,
        download_name=f"{utl.sha256(base64.b64encode(output.read()).decode('utf-8'))}.png"
    )
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8585)