#HTTP Server template

from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 1234 # Maybe set this to 1234

Torstein = "C:\\Kode\\GitHub\\KBE2\\KBE2\\" #location
Aashild = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\assig1\\KBE2-Chair-Design\\" #location
#yourLocation = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\DFAs" #this must be changed
yourLocation = Aashild #must be changed after whom is using it

#definfing parameters to be changed by the custommer
leg_length1 = "leg length"
leg_side1 = "leg width"
seat_side1 = "seat width"
back_height1 = "back height"
back_shape1 = "back shape"
#back_shape_color1 = "back shape color"
chair_color = "chair color"
back_shape_material1 = "back shape material"
chair_material1 = "chair material"
number_chair1 = "number of chairs"
fname1 = "first name"
lname1 = "last name"
email1 = "e-mail"
pnumber1 = "phone number"

custom_parameters = [leg_length1, leg_side1, seat_side1, back_height1, back_shape1, chair_color, back_shape_material1, chair_material1, number_chair1, fname1, lname1, email1, pnumber1]
print_order = "Hei på deg, dette fungerer ikke."

# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):


	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()


	def do_GET(s):

		global leg_length1, leg_side1, seat_side1, back_height1, back_shape1, back_shape_color1, chair_color, back_shape_material1, chair_material1, number_chair1, fname1, lname1, email1, pnumber1, print_order
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
		elif path.find("/orderChair") != -1:
			s.wfile.write(bytes("<!DOCTYPE html><html><head>", 'utf-8'))
			s.wfile.write(bytes("<title>Chair Design</title>", 'utf-8'))
			s.wfile.write(bytes("</head><body>", 'utf-8'))
			s.wfile.write(bytes("<h1>Product details</h1>", 'utf-8'))
			s.wfile.write(bytes("<p>Welcome to our chair company. Here you can customize a chair for your home!</p>", 'utf-8'))
			s.wfile.write(bytes("<p> Write your desired parameters. </p>", 'utf-8'))

			#unsecure about next line, we need to figure out what it does and what we need
			s.wfile.write(bytes("<form action='/yourOrder' method='post'>", 'utf-8'))

			#starting with the inputs
			s.wfile.write(bytes("<label for='leg_length'>Length of the legs [cm]:</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='leg_length' name='leg_length' value=" + str(leg_length1) +"><br><br>", 'utf-8'))
			s.wfile.write(bytes("<label for='leg_side'>Width of the legs [cm]: <br>(note that the legs is quadratic)</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='leg_side' name='leg_side' value=" + leg_side1 + "><br><br>", 'utf-8'))
			s.wfile.write(bytes("<label for='seat_side'>Width of the seat [cm]:<br>(note that the seat is quadratic)</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='seat_side' name='seat_side' value=" + seat_side1 + "><br><br>", 'utf-8'))
			s.wfile.write(bytes("<label for='back_height'>Height  of the back [cm]:</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='back_height' name='back_height' value=" + back_height1+ "><br><br>", 'utf-8'))
			
			#starting with the option boxes
			s.wfile.write(bytes("<label for='back_shape'> Choose the shape in the back: </label>", 'utf-8'))
			s.wfile.write(bytes("<select id='back_shape' name='back_shape'>", 'utf-8'))
			s.wfile.write(bytes("<option value='circle'>Circles</option>", 'utf-8'))  
			s.wfile.write(bytes("<option value='square'>Square</option>", 'utf-8'))  
			s.wfile.write(bytes("<option value='cross'>Cross</option>", 'utf-8'))  
			s.wfile.write(bytes("</select> <br><br>", 'utf-8'))  

			""" #not a specific color for the shape in the back
			s.wfile.write(bytes("<label for='back_shape_color'> The color of the shape in the back: </label>", 'utf-8'))  
			s.wfile.write(bytes("<select id='back_shape_color' name='back_shape_color'>", 'utf-8'))  
			s.wfile.write(bytes("<option value='RED'>Red</option>", 'utf-8'))  
			s.wfile.write(bytes("<option value='BLUE'>Blue</option>", 'utf-8'))  
			s.wfile.write(bytes("<option value='YELLOW'>Yellow</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='WHITE'>White</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='BROWN'>Brown</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='BLACK'>Black</option>", 'utf-8'))
			s.wfile.write(bytes("</select><br><br>", 'utf-8'))
			"""

			s.wfile.write(bytes("<label for='chair_color'> The color for the chair: </label>", 'utf-8'))
			s.wfile.write(bytes("<select id='chair_color' name='chair_color'>", 'utf-8')) 
			s.wfile.write(bytes("<option value='RED'>Red</option>", 'utf-8')) 
			s.wfile.write(bytes("<option value='BLUE'>Blue</option>", 'utf-8')) 
			s.wfile.write(bytes("<option value='YELLOW'>Yellow</option>", 'utf-8')) 
			s.wfile.write(bytes("<option value='WHITE'>White</option>", 'utf-8')) 
			s.wfile.write(bytes("<option value='BROWN'>Brown</option>", 'utf-8')) 
			s.wfile.write(bytes("<option value='BLACK'>Black</option>", 'utf-8'))  
			s.wfile.write(bytes("</select><br><br>", 'utf-8'))

			s.wfile.write(bytes("<label for='back_shape_material'> The material for the shape: </label>", 'utf-8'))
			s.wfile.write(bytes("<select id='back_shape_material' name='back_shape_material'>", 'utf-8'))
			s.wfile.write(bytes("<option value='Wood'>Wood</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Plastic'>Plastic</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Oak'>Oak</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Steel'>Steel</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Aluminum'>Aluminum</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Gold'>Gold</option>", 'utf-8'))
			s.wfile.write(bytes("</select><br><br>", 'utf-8'))

			s.wfile.write(bytes("<label for='chair_material'> The material for the chair: </label>", 'utf-8'))
			s.wfile.write(bytes("<select id='chair_material' name='chair_material'>", 'utf-8'))
			s.wfile.write(bytes("<option value='Wood'>Wood</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Plastic'>Plastic</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Oak'>Oak</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Steel'>Steel</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Aluminum'>Aluminum</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Gold'>Gold</option>", 'utf-8'))
			s.wfile.write(bytes("</select><br><br><br>", 'utf-8'))

			s.wfile.write(bytes("<label for='number_chair'>Number of chairs to order: </label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='number_chair' name='number_chair' value=" + number_chair1 + "><br><br>", 'utf-8'))

			s.wfile.write(bytes("<fieldset><legend>Personalia:</legend>", 'utf-8'))
			s.wfile.write(bytes("<label for='fname'>First name:</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='fname' name=fname' value="+fname1+"><br>", 'utf-8'))
			s.wfile.write(bytes("<label for='lname'>Last name:</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='lname' name='lname' value="+lname1+"><br>", 'utf-8'))
			s.wfile.write(bytes("<label for='email'>E-mail:</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='email' name='email' value="+email1+"><br>", 'utf-8'))
			s.wfile.write(bytes("<label for='pnumber'>Phone number:</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='pnumber' name='pnumber' value="+pnumber1+"><br><br>", 'utf-8'))

			s.wfile.write(bytes("</fieldset><br>", 'utf-8'))
			s.wfile.write(bytes("<p>Click 'Submit' to put your chair in the shopping cart:", 'utf-8'))
			s.wfile.write(bytes("<input type='submit' value='Submit'></p>", 'utf-8'))
			s.wfile.write(bytes("<p>Click 'Save' to save your design for later:", 'utf-8'))
			s.wfile.write(bytes("<input type='submit' value='Save'>", 'utf-8'))
			s.wfile.write(bytes("</p></form> </body></html>", 'utf-8'))
			
		elif path.find("/yourOrder") != -1:
			s.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
			s.wfile.write(bytes('<form action="/yourOrder" method="post">', 'utf-8'))
			
			s.wfile.write(bytes('<p>The following parameters line has arrived: ' + print_order +'</p>', 'utf-8'))
			
			#s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
			s.wfile.write(bytes('</form></body></html>', 'utf-8'))
		
		#s.wfile.write(bytes("", 'utf-8'))
		#s.wfile.write(bytes("", 'utf-8'))

		#s.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
		#s.wfile.write(bytes('</body></html>', "utf-8"))
		elif path.find("/info") != -1:
			s.wfile.write(bytes('<html><head><title>Cool interface.</title><meta http-equiv="refresh" content="3"></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>Info: Hello!.</p>" + str(i), "utf-8"))
			s.wfile.write(bytes('"</body></html>', "utf-8"))
			
	def do_POST(s):
		#allowing us to eddit the custom parameters
		global custom_parameters

		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
		# Check what is the path
		path = s.path
		print("Path: ", path)
		print("hei på deg!!")
		if path.find("/yourOrder") != -1:
			
			#for debugging
			print("Nå er vi i post-method. ")

			#copied form practise lecture -- is this nessesary?
			content_len = int(s.headers.get('Content-Length'))
			post_body = s.rfile.read(content_len)
			param_line = post_body.decode()
			print("Body: ", param_line)

			#making a string to print
			global print_order, yourLocation
			print_order = ""
			#getting the parameter values
			key_val_pair = param_line.split('&')							#splitting the string at "&"
			for i in range(len(custom_parameters)): 						#itterating through the custom_parameter list
				print_order += str(custom_parameters[i]) 					#before changing the parameters, adding the to a string for printing
				print_order +=": " 											#for a nice print
				custom_parameters[i] = key_val_pair[i].split('=')[1]		#spliting at "=" to only get the value
				if ' ' in custom_parameters[i]: 							#the last parameter has "HTTP/1.1" and we dont want it
					custom_parameters[i] = custom_parameters[i].split(" ")[0] #spliting to get rid of it ^
				print_order += str(custom_parameters[i])
				print_order += ", "

			#need to find which shape the order has in the back
			if back_shape1 == "circle": 
				#the shape is a cicle
				f = open(yourLocation+"DFAtemplate\\chairdesign_circle_template.dfa", 'r')
				templatefile = f.read()
				f.close()
			elif back_shape1 == "cross":
				#the shape is a cross
				f = open(yourLocation+"DFAtemplate\\chairdesign_cross_template.dfa", 'r')
				templatefile = f.read()
				f.close()
			elif back_shape1 == "square":
				#the shape is a square
				f = open(yourLocation+"DFAtemplate\\chairdesign_rectangle_template.dfa", 'r')
				templatefile = f.read()
				f.close()
			else:
				print("the shape in the back is not recognised.")
				break
			
			param = ["<leg_length>","<leg_side>","<seat_side>","<height_back>","<color_chair>","<"]
			s.do_GET()

		if path.find("/"):
			content_len = int(s.headers.get('Content-Length'))
			post_body = s.rfile.read(content_len)
			param_line = post_body.decode()
			print("Body: ", param_line)
			s.wfile.write(bytes('<p>' + param_line + '</p>', 'utf-8'))
 
if __name__ == '__main__':
	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
