import json
from flask import Flask, jsonify, render_template, request, Response


app = Flask(__name__)




with open('skincarelist.JSON') as json_data:
    d = json.load(json_data)
    list_of_skincarelist = []
    for data in d['skincarelist']:
    	list_of_skincarelist.append(data)

with open('skincarelist1.JSON') as skincarelist1_data:
	a = json.load(skincarelist1_data)
	list_of_skincare = []
	for skincarelist1 in a['skincare']:
		list_of_skincare.append(skincarelist1)
	print("list_of_skincare: ", list_of_skincare)

@app.route('/', methods =['GET'])
def home():
	return render_template("index.html")

@app.route('/skincarelist', methods =['GET'])
def all_skincarelist():
	typefilter = request.args.get('type')
	if (typefilter == 'json'):
		return jsonify(d)
	return render_template("index.html",list_data=list_of_skincarelist)

@app.route('/skincarelist/<string:skincare_id>', methods =['GET'])
def skincare_by_id(skincare_id):
	emp = [skincarelist for skincarelist in list_of_skincarelist if skincarelist['skincareid'] == skincare_id]
	typefilter = request.args.get('type')
	if (typefilter == 'json'):
		return jsonify(emp)
	return render_template("index.html",list_data=emp)

@app.route('/skincarelist/<string:skincare_id>/skincarelist1', methods =['GET'])
def skincarelist1_by_skincare_id(skincare_id):
	skincare_skincarelist1 = [skincare for skincare in list_of_skincare if skincare['skincareid'] == skincare_id]
	# print("skincare_skincarelist1: ", str(skincare_skincarelist1))
	skincarelist1 = skincare_skincarelist1[0]['skincarelist1']
	# print("skincare_skincarelist1: ", str(skincarelist1))
	typefilter = request.args.get('type')
	if (typefilter == 'json'):
		return jsonify(skincare_skincarelist1)
	return render_template("index.html", list_skincarelist1_data=skincarelist1, skincare_id=skincare_id)

@app.route('/skincarelist/<string:skincare_id>/skincarelist1/<string:skincarelist1_id>', methods =['GET'])
def skincarelist1_by_skincare_id_skincarelist1_id(skincare_id, skincarelist1_id):
	skincare_skincarelist1 = [skincare for skincare in list_of_skincare if skincare['skincareid'] == skincare_id]
	# print("skincare_skincarelist1: ", str(skincare_skincarelist1))
	# print("skincare_skincarelist1[0]: ", str(skincare_skincarelist1[0]))
	# print("skincarelist1: ", str(skincare_skincarelist1[0]['skincarelist1']))
	arm = [skincarelist1 for skincarelist1 in skincare_skincarelist1[0]['skincarelist1'] if skincarelist1['skincarelist1id'] == skincarelist1_id]
	print("single arm: ", arm)
	typefilter = request.args.get('type')
	if (typefilter == 'json'):
		return jsonify(arm)
	return render_template("index.html", list_skincarelist1_data=arm, skincare_id=skincare_id)

if __name__ == '__main__':
	 app.run(host='0.0.0.0', port=7000)