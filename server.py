from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/', methods=['GET'])
def index():
   return render_template('index.html')


## API 역할을 하는 부분
@app.route('/order', methods=['GET'])
def order_get():
    item = request.args.get('item_give')
    result = list(db.orders.find({'item':item}, {'_id':0}))
    print(result)
    return jsonify({'result':'success', 'orders':result})

@app.route('/order', methods=['POST'])
def order_post():
   name = request.form['name_give']
   count = request.form['count_give']
   address = request.form['address_give']
   phone = request.form['phone_give']
   item = request.form['item_give']

   db.orders.insert_one({'name':name, 'count':count, 'address':address,
                         'phone': phone, 'item': item})

   return jsonify({'result':'success'})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)