import redis
from flask import Flask, jsonify, request
import csv

def f():
    file = open('Test.csv')
    data = csv.reader(file)

    rlist = []
    i = 0
    enames = ['id','year','rain']
    for line in data:
        rlist.append({})
        for j in range(len(line)):
            if j == 0:
                rlist[i][enames[j]] = int(line[j])
            else:
                if float(line[j])%1 == 0:
                    rlist[i][enames[j]] = int(line[j])
                else:
                    rlist[i][enames[j]] = float(line[j])

        i = i + 1

    return rlist

def g(start=0,end=0):
    full_data = f()

    if start:
        if end:
            subdata = []
            for i in range(len(full_data)):
                if full_data[i]['year'] >= int(start) and full_data[i]['year'] <= int(end):
                    subdata.append(full_data[i])
        else:
            subdata = []
            for i in range(len(full_data)):
                if full_data[i]['year'] >= int(start):
                    subdata.append(full_data[i])
    else:
        if end:
            subdata = []
            for i in range(len(full_data)):
                if full_data[i]['year'] <= int(end):
                    subdata.append(full_data[i])
        else:
            subdata = full_data

    return subdata

def h(limit=len(f()),offset=0):
    full_data = f()

    subdata = []
    if limit:
        if offset:
            subdata = full_data[int(offset):int(offset) + max(min(int(limit),len(full_data)),0)]
        else:
            subdata = full_data[0:max(min(int(limit),len(full_data)),0)]
    else:
        if offset:
            subdata = full_data[int(offset):]
        else:
            subdata = full_data
    return subdata

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

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
            return 'Error: id must be within the range of the length of the dataset\n'
    except:
        return 'Error: id must be a number\n'

@app.route('/rain/<time>/<int:value>',methods=['GET'])
def get_rain_time(time,value):
    for i in range(len(f())):
        if f()[i][time] == value:
            return jsonify(f()[i])

    return 'Error: time value entered was not in the dataset. Please try again\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
