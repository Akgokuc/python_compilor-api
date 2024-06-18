from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import sys,io

app = Flask(__name__)
CORS(app)

@app.route('/api/get')
def create_gwt():
        data='hello'

        return data

# POST endpoint to create a new post
@app.route('/api/posts', methods=['POST'])
@cross_origin()
def create_post():
        data = request.data.decode('utf-8')

        original_stdout = sys.stdout

       
        captured_output = io.StringIO()
        sys.stdout = captured_output

      
        exec(data)

 
        sys.stdout = original_stdout

 
        output_value = captured_output.getvalue()
        return output_value

if __name__ == '__main__':
    app.run(debug=True)
