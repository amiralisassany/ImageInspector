from PIL import Image
import io
import base64
from flask import Flask, request, send_file, jsonify
import json
from core import Handler
from utils import utl
from config import Config

import os,sys
sys.path.append(os.path.abspath("plugins/"))
plugins = list(map(lambda x: x.replace(".py", ""), os.listdir('plugins/')))


# API
app = Flask(__name__)
@app.route('/plugins',methods=["GET"])
def plugins_r():
    return jsonify(plugins)

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
        return jsonify({'error': 'Plugin is missing'}), 400
 
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
if __name__ == '__main__' :
    app.run(debug=Config.debug,host=Config.ip,port=Config.port)
