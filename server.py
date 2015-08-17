from flask import Flask, request
from twilio import twiml
#twimil is the python twilio helper library. 

app = Flask(__name__)

friends = {
	"+16509964810": "Gowri", 
	"+14158166313" : "Susan",
	"6466480603": "Ashley",
}

@app.route("/", methods=["GET", 'POST'])
def index(): 
	# resp=twiml.Response()
	# resp.message("Hackbright XI is awesome!")
	# return str(resp)

	# this would take a look at who the caller was, and then generate the twimil based on who the caller is. 
	from_number=request.values.get('From')
	if from_number in friends: 
		name = friends[from_number]
	else: 
		name = "Monkey"
	message = "hello {}!!, thanks for the message!".format(name)
	resp = twiml.Response()
	resp.message(message)
	return str(resp)


if __name__=="__main__": 
	app.run(debug=True)





