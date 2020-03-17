from flask import Flask
from dl_ocr import text_extractor

app = Flask(__name__)


@app.route('/ocr/')
def get_text():
    text = dict()
    text_array, state, state_name, address, name, license_number, dob, expiry_dt = text_extractor()

    text['state'] = state_name
    text['name'] = name
    text['address'] = address
    text['id'] = license_number
    text['dob'] = dob
    text['expiry_dt'] = expiry_dt

    return text


if __name__ == "__main__":
    app.run(host='localhost', port=5000)
