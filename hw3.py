from flask import Flask, request, jsonify
from hw1.hw1 import f,g,h

app = Flask(__name__)

@app.route('/rain',methods=['GET'])
def get_rain_funcs():
    limit = request.args.get('limit')
    offset = request.args.get('offset')
    start = request.args.get('start')
    end = request.args.get('end')

    if ((limit or offset) and not (start or end)):
        return jsonify(h(limit,offset))

    elif ((start or end) and not (limit or offset)):
        return jsonify(g(start,end))

    elif ((start or end) and (limit or offset)):
        return 'Error: Start and End cannot be used in conjunction with Limit and Offset\n'

    else:
        return jsonify(f())

@app.route('/rain/<int:id>',methods=['GET'])
def get_rain_id(id):
    try:
        id = int(id)
        if id < len(f()) and id>=0:
            data = f()[id]
            return jsonify(data)
        else:
            return 'Error: id must be within the range of the length of the dataset'
    except:
        return 'Error: id must be a number'

@app.route('/rain/<time>/<int:value>',methods=['GET'])
def get_rain_time(time,value):
    for i in range(len(f())):
        if f()[i][time] == value:
            return jsonify(f()[i])

    return 'Error: time value entered was not in the dataset. Please try again'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='5000')
