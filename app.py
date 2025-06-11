from flask import Flask, request, jsonify, send_file, render_template
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import os
import base64

app = Flask(__name__)

# Tạo thư mục để lưu trữ file
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Tạo cặp khóa RSA
def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    with open("private_key.pem", "wb") as f:
        f.write(private_key)
    with open("public_key.pem", "wb") as f:
        f.write(public_key)
    
    return private_key, public_key

# Tạo chữ ký số
def sign_file(file_data, private_key):
    key = RSA.import_key(private_key)
    hash_obj = SHA256.new(file_data)
    signature = pkcs1_15.new(key).sign(hash_obj)
    return base64.b64encode(signature).decode()

# Xác thực chữ ký
def verify_signature(file_data, signature, public_key):
    key = RSA.import_key(public_key)
    hash_obj = SHA256.new(file_data)
    try:
        pkcs1_15.new(key).verify(hash_obj, base64.b64decode(signature))
        return True
    except (ValueError, TypeError):
        return False

@app.route('/')
def index():
    return render_template('sender.html')

@app.route('/receiver')
def receiver():
    return render_template('receiver.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Không tìm thấy file'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Không có file được chọn'}), 400
    
    # Đọc nội dung file
    file_data = file.read()
    
    # Tạo chữ ký số
    private_key, public_key = generate_key_pair()
    signature = sign_file(file_data, private_key)
    
    # Lưu file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, 'wb') as f:
        f.write(file_data)
    
    return jsonify({
        'message': 'File đã được tải lên thành công',
        'signature': signature,
        'public_key': public_key.decode()
    })

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File không tồn tại'}), 404
    
    return send_file(file_path, as_attachment=True)

@app.route('/verify', methods=['POST'])
def verify_file():
    if 'file' not in request.files or 'signature' not in request.form or 'public_key' not in request.form:
        return jsonify({'error': 'Thiếu thông tin cần thiết'}), 400
    
    file = request.files['file']
    signature = request.form['signature']
    public_key = request.form['public_key'].encode()
    
    file_data = file.read()
    is_valid = verify_signature(file_data, signature, public_key)
    
    return jsonify({
        'is_valid': is_valid,
        'message': 'Chữ ký hợp lệ' if is_valid else 'Chữ ký không hợp lệ'
    })

@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify(files)

if __name__ == '__main__':
    app.run(debug=True) 