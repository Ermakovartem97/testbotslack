from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

# ������� ��������
@app.route('/webhook')
def hello_slack():
    # �������� ������ �� �������
    request_json = request.get_json(silent=True, force=True)
    # ��� ��� ��� ������� ������ � ������ � ����� ����� dict ������ ������, ����� ���� ������
    # �������� ��� request_json -> response_body_json
    ...
    response_body = json.dumps(response_body_json)
    # ��������� ��� � ���������� �������
    response = make_response(response_body)
    response.headers['Content-Type'] = 'application/json'
    # � �������
    return response

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')