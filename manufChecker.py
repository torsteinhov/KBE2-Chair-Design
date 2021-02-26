#HTTP Server template

from http.server import BaseHTTPRequestHandler, HTTPServer

import time
import requests
import json

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 4321 # Maybe set this to 1234


#definfing parameters upper and lower limits
leg_lengthMax = 200
leg_lengthMin = 55
leg_sideMax = 15
leg_sideMin = 3
seat_sideMax = 150
seat_sideMin = 30
back_heightMax = 150
back_heightMin = 20

chair_color = ['RED', 'GREEN', 'BROWN', 'BLACK'] # a list with the avaliable colors
back_shape_material = [] #a list with avaliable materials
chair_material = [] #a list with avaliable matrials
# ??  number_chair = # check if there is enough materials for number of chair orders

#custom_parameters = [leg_length1, leg_side1, seat_side1, back_height1, chair_color, back_shape_material1, chair_material1, number_chair1]

# putting the constraints from the manufacturing department into a list
production_intz_param = [leg_lengthMax, leg_lengthMin, leg_sideMax, leg_sideMin, seat_sideMax, seat_sideMin, back_heightMax, back_heightMin, chair_color,back_shape_material, chair_material]



    
# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):


	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()


	def do_GET(s):

		#global leg_length1, leg_side1, seat_side1, back_height1, back_shape1, back_shape_color1, chair_color, back_shape_material1, chair_material1, number_chair1, fname1, lname1, email1, pnumber1, print_order
		"""Respond to a GET request."""
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
		# Check what is the path
		path = s.path
		
		#making it possible to get the global variables
		#s.wfile.write(bytes("<>", 'utf-8'))
		if path.find("/") != -1 and len(path) == 1:
			s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
			s.wfile.write(bytes('</body></html>', "utf-8"))
		elif path.find("/setParams") != -1:

			s.wfile.write(bytes("<!DOCTYPE html><html><body>", 'utf-8'))
			s.wfile.write(bytes("<h2>Product details intervals and available choises</h2>", 'utf-8'))
			s.wfile.write(bytes("<p>Please fill in details about the production below. </p>", 'utf-8'))

			s.wfile.write(bytes('<form action="/parametersSet" method="post">', 'utf-8'))

			#intervals for leg length, leg side, seat side, back height
			s.wfile.write(bytes("<p> Write maximum and minimum parameters in cm. </p>", 'utf-8'))

			s.wfile.write(bytes('<label for="leg_lengthUp">Max leg length:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="leg_lengthUp" name="leg_lengthUp" value='+ str(leg_lengthMax) +'><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="leg_lengthLow">Min leg length:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="leg_lengthLow" name="leg_lengthLow" value='+ str(leg_lengthMin) +'><br><br>', 'utf-8'))

			s.wfile.write(bytes('<label for="leg_sideUp">Max leg width:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="leg_sideUp" name="leg_sideUp" value='+ str(leg_sideMax) +'><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="leg_sideLow">Min leg width:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="leg_sideLow" name="leg_sideLow" value='+ str(leg_sideMin) +'><br><br>', 'utf-8'))

			s.wfile.write(bytes('<label for="seat_sideUp">Max seat width:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="seat_sideUp" name="seat_sideUp" value='+ str(seat_sideMax) +'><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="seat_sideLow">Min seat width:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="seat_sideLow" name="seat_sideLow" value='+ str(seat_sideMin) +'><br><br>', 'utf-8'))

			s.wfile.write(bytes('<label for="back_heightUp">Max back height:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="back_heightUp" name="back_heightUp" value='+ str(back_heightMax) +'><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="back_heightLow">Min back height:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="back_heightLow" name="back_heightLow" value='+ str(back_heightMin) +'><br><br>', 'utf-8'))

			#chair colors
			s.wfile.write(bytes('<p>Select the available colors for the chair:</p>', 'utf-8'))
			s.wfile.write(bytes('<input type="checkbox" id="chair_color" name="chair_color" value="RED">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_color"> Red</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_color" name="chair_color" value="BLUE">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_color"> Blue</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_color" name="chair_color" value="YELLOW">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_color"> Yellow</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_color" name="chair_color" value="WHITE">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_color"> White</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_color" name="chair_color" value="BROWN">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_color"> Brown</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_color" name="chair_color" value="BLACK">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_color"> Black</label><br><br>', 'utf-8'))

			#back shape material
			s.wfile.write(bytes('<p>Select the available material for the back shape:</p>', 'utf-8'))
			s.wfile.write(bytes('<input type="checkbox" id="back_shape_material" name="back_shape_material" value="Wood">', 'utf-8'))
			s.wfile.write(bytes('<label for="back_shape_material"> Wood</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="back_shape_material" name="back_shape_material" value="Plastic">', 'utf-8'))
			s.wfile.write(bytes('<label for="back_shape_material"> Plastic</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="back_shape_material" name="back_shape_material" value="Oak">', 'utf-8'))
			s.wfile.write(bytes('<label for="back_shape_material"> Oak</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="back_shape_material" name="back_shape_material" value="Steel">', 'utf-8'))
			s.wfile.write(bytes('<label for="back_shape_material"> Steel</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="back_shape_material" name="back_shape_material" value="Aluminum">', 'utf-8'))
			s.wfile.write(bytes('<label for="back_shape_material"> Brown</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="back_shape_material" name="back_shape_material" value="Gold">', 'utf-8'))
			s.wfile.write(bytes('<label for="back_shape_material"> Gold</label><br><br>', 'utf-8'))

			#chair_material
			s.wfile.write(bytes('<p>Select the available material for the chair:</p>', 'utf-8'))
			s.wfile.write(bytes('<input type="checkbox" id="chair_material" name="chair_material" value="Wood">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_material"> Wood</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_material" name="chair_material" value="Plastic">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_material"> Plastic</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_material" name="chair_material" value="Oak">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_material"> Oak</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_material" name="chair_material" value="Steel">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_material"> Steel</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_material" name="chair_material" value="Aluminum">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_material"> Brown</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_material" name="chair_material" value="Gold">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_material"> Gold</label><br><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="submit" value="Submit"></form>', 'utf-8'))
			s.wfile.write(bytes('</body></html>', 'utf-8'))
			s.wfile.write(bytes('', 'utf-8'))
		
		elif path.find("/parametersSet") != -1:
			s.wfile.write(bytes('<form action="/parametersSet" method="post">', 'utf-8'))
			s.wfile.write(bytes('<!DOCTYPE html><html><head>', 'utf-8'))
			s.wfile.write(bytes('<title>new intervals and choises</title>', 'utf-8'))
			s.wfile.write(bytes('</head><body>', 'utf-8'))
			s.wfile.write(bytes('<h1>The new intervals and choises for the customer.</h1>', 'utf-8'))
			s.wfile.write(bytes('<p>The following parameters have been set: </p>', 'utf-8'))
			s.wfile.write(bytes('<p>Leg length max: '+ str(production_intz_param[0]) +'</p>', 'utf-8'))
			s.wfile.write(bytes('<p>Leg length min: '+ str(production_intz_param[1]) +'</p>', 'utf-8'))
			s.wfile.write(bytes('<p>Leg side max: '+ str(production_intz_param[2]) +'</p>', 'utf-8'))
			s.wfile.write(bytes('<p>Leg side min: '+ str(production_intz_param[3]) +'</p>', 'utf-8'))
			s.wfile.write(bytes('<p>Seat side max: '+ str(production_intz_param[4]) +'</p>', 'utf-8'))
			s.wfile.write(bytes('<p>Seat side min: '+ str(production_intz_param[5]) +'</p>', 'utf-8'))
			s.wfile.write(bytes('<p>Back height max: '+ str(production_intz_param[6]) +'</p>', 'utf-8'))
			s.wfile.write(bytes('<p>Back height min: '+ str(production_intz_param[7]) +'</p>', 'utf-8'))
			s.wfile.write(bytes('<p>Chair colors: '+ str(production_intz_param[8]) +'</p>', 'utf-8'))
			s.wfile.write(bytes('<p>Back shape material: '+ str(production_intz_param[9]) +'</p>', 'utf-8'))
			s.wfile.write(bytes('<p>Chair material: '+ str(production_intz_param[10]) +'</p>', 'utf-8'))
			#s.wfile.write(bytes('<p>:'+  +'</p>', 'utf-8'))
			s.wfile.write(bytes('</body></html>', 'utf-8'))
		
	def do_POST(s):
		#allowing us to eddit the custom parameters
		global production_intz_param

		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
		# Check what is the path
		path = s.path
		print("Path: ", path)

		if path.find("/parametersSet") != -1:
			#s.wfile.write(bytes('<form action="/updatedIntzAre" method="get">', 'utf-8'))
			#for debugging
			print("Nå er vi i post-method. ")

			#copied form practise lecture -- is this nessesary?
			content_len = int(s.headers.get('Content-Length'))
			post_body = s.rfile.read(content_len)
			param_line = post_body.decode()
			print("Body: ", param_line)
		
			production_intz_param[8] = [] #chair color
			production_intz_param[9] = [] #back shape material
			production_intz_param[10] = [] #chair material
			#preparing for new intervals and choises
			
			#getting the parameter values
			key_val_pair = param_line.split('&')						#splitting the string at "&"
			#print("key_val_pair: ",key_val_pair)
			for i in range(len(key_val_pair)): 						#itterating through the custom_parameter list
				
				#taking care of the optionboxes
				if key_val_pair[i].split('=')[0] == 'chair_color':
					production_intz_param[8].append(key_val_pair[i].split('=')[1])
				elif key_val_pair[i].split('=')[0] == 'back_shape_material':
					production_intz_param[9].append(key_val_pair[i].split('=')[1])
				elif key_val_pair[i].split('=')[0] == 'chair_material':
					production_intz_param[10].append(key_val_pair[i].split('=')[1])
					if ' ' in key_val_pair[i]: 							#the last parameter has "HTTP/1.1" and we dont want it
						production_intz_param[10] = key_val_pair[i].split('=')[1].split(" ")[0] #spliting to get rid of it ^
				else:
					production_intz_param[i] = int(key_val_pair[i].split('=')[1])		#splitting at "=" to only get the value
				
			print("production_intz_param: ", production_intz_param)

			#upload data til fuseki
			s.setConstrain(production_intz_param)
			 
			s.do_GET()

	def setConstrain(self, production_intz_param):
		URL = "http://127.0.0.1:3030/chair_design/update"
  
		# Query that deletes previous values.
		deleteQuery = 'PREFIX kbe:<http://www.kbe.com/chair_design.owl#> '+\
				'DELETE'+\
				'{'+\
				'?back_1 kbe:hasBackHeightMax ?backHeightMax.'+\
				'?back_1 kbe:hasBackHeightMin ?backHeightMin.'+\
				'?chair_1 kbe:hasColor ?chairColor.'+\
				'?chair_1 kbe:hasMaterial ?chairMaterial.'+\
				'?leg_1 kbe:hasLegLengthMax ?legLengthMax.'+\
				'?leg_1 kbe:hasLegLengthMin ?legLengthMin.'+\
				'?leg_1 kbe:hasLegSideMax ?legSideMax.'+\
				'?leg_1 kbe:hasLegSideMin ?legSideMin.'+\
				'?shape_1 kbe:hasMaterial ?shapeMaterial.'+\
				'?shape_1 kbe:hasShape ?shape.'+\
				'?seat_1 kbe:hasSeatSideMax ?seatSideMax.'+\
				'?seat_1 kbe:hasSeatSideMin ?seatSideMin.'+\
				'}'+\
				'WHERE'+\
				'{'+\
				'?back_1 kbe:hasBackHeightMax ?backHeightMax.'+\
				'?back_1 kbe:hasBackHeightMin ?backHeightMin.'+\
				'?chair_1 kbe:hasColor ?chairColor.'+\
				'?chair_1 kbe:hasMaterial ?chairMaterial.'+\
				'?leg_1 kbe:hasLegLengthMax ?legLengthMax.'+\
				'?leg_1 kbe:hasLegLengthMin ?legLengthMin.'+\
				'?leg_1 kbe:hasLegSideMax ?legSideMax.'+\
				'?leg_1 kbe:hasLegSideMin ?legSideMin.'+\
				'?shape_1 kbe:hasMaterial ?shapeMaterial.'+\
				'?shape_1 kbe:hasShape ?shape.'+\
				'?seat_1 kbe:hasSeatSideMax ?seatSideMax.'+\
				'?seat_1 kbe:hasSeatSideMin ?seatSideMin.'+\
				'}'

		PARAMS = {'update': deleteQuery}
		# sending get request and saving the response as response object 
		r = requests.post(url = URL, data = PARAMS)
		print("Result of DELETE query:", r.text)
	
		insertQuery = 'PREFIX kbe:<http://www.kbe.com/chair_design.owl#>' +\
				'PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>'+\
				'INSERT'+\
				'{'+\
				'?leg_1 kbe:hasLegLengthMax "'+ str(production_intz_param[0])+'"^^xsd:int.'+\
				'?leg_1 kbe:hasLegLengthMin "'+ str(production_intz_param[1])+'"^^xsd:int.'+\
				'?leg_1 kbe:hasLegSideMax "'+ str(production_intz_param[2])+'"^^xsd:int.'+\
				'?leg_1 kbe:hasLegSideMin "'+ str(production_intz_param[3])+'"^^xsd:int.'+\
				'?seat_1 kbe:hasSeatSideMax "'+ str(production_intz_param[4])+'"^^xsd:int.'+\
				'?seat_1 kbe:hasSeatSideMin "'+ str(production_intz_param[5])+'"^^xsd:int.'+\
				'?back_1 kbe:hasBackHeightMax "'+ str(production_intz_param[6])+'"^^xsd:int.'+\
				'?back_1 kbe:hasBackHeightMin "'+ str(production_intz_param[7])+'"^^xsd:int.'+\
				'?shape_1 kbe:hasShape "circle"^^xsd:str.'+\
				'?chair_1 kbe:hasColor "'+ str(production_intz_param[8])+'"^^xsd:str.'+\
				'?shape_1 kbe:hasMaterial "'+ str(production_intz_param[9])+'"^^xsd:str.'+\
				'?chair_1 kbe:hasMaterial "'+ str(production_intz_param[10])+'"^^xsd:str.'+\
				'}'+\
				'WHERE'+\
				'{'+\
				'?leg_1 a kbe:Leg.'+\
				'?seat_1 a kbe:Seat.'+\
				'?back_1 a kbe:Back.'+\
				'?chair_1 a kbe:Chair.'+\
				'?shape_1 a kbe:Shape.'+\
				'}'
		# defining a query params 
		PARAMS = {'update': insertQuery} 
		r = requests.post(url = URL, data = PARAMS)
		#Checking the result
		print("Result of INSERT query:", r.text)
	
	"""
	production_intz_param = 
	[leg_lengthMax, 
	leg_lengthMin, 
	leg_sideMax, 
	leg_sideMin, 
	seat_sideMax, 
	seat_sideMin, 
	back_heightMax, 
	back_heightMin, 
	chair_color,
	back_shape_material, 
	chair_material]
	"""

if __name__ == '__main__':
	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
