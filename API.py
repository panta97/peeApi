from flask import Flask, request, jsonify
from pyknow import Fact
from urineColors import urineColor, AI

app = Flask(__name__)

@app.route('/',methods=['POST'])
def API_example():
    urine = request.get_json().get('urine',None)
    AI.reset()
    AI.declare(urineColor(colorCode=urine))
    AI.run()
    return jsonify({'AI_response': AI.response})



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=8080)