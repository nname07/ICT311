from flask import Flask, render_template
from insert import insert_app  # ถ้าคุณมีไฟล์ insert.py ที่ใช้ Blueprint

app = Flask(__name__)

# ลงทะเบียน Blueprint สำหรับ insert
app.register_blueprint(insert_app)

# หน้าแรกของระบบ
@app.route('/')
def index():
    return render_template("index.html")

# หน้ารวมบริการทั้งหมด
@app.route('/services')
def services():
    return render_template("services.html")

# หน้าย่อยสำหรับบริการแต่ละประเภท
@app.route('/services/<service_name>')
def service_detail(service_name):
    try:
        return render_template(f"service_{service_name}.html")
    except:
        return "ไม่พบหน้าบริการที่คุณต้องการ", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
