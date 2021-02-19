# DFAServer (pk)
from http.server import BaseHTTPRequestHandler, HTTPServer

import time
import requests
import json

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 1234 # Maybe set this to 1234

#definding variables for the file finding
PATH_TO_DFA = "C:\\Users\\Hilde\\Documents\\NTNU\\Automatisering_i_ingeniorarbeid\\DFAs\\"
DFA_TEMPLATE_FILE_NAME = "table_template_DFA.dfa"
NEW_DFA_FILE_NAME = "table_for_customer_auto.dfa"

#definding my parameters
#I have added a 1, so it won't be in conflict with the parameter names in the string from the "webpage"
tableHeight1 = "the table height"
topDia1 = "The diameter of table"
topColor1 = "the color of the topPlate"
bearingColor1 = "the color of the bearing"
baseColor1 = "the color of the base"
topMaterial1 = "the material of the topPlate"
bearingMaterial1 = "the material of the bearing"
baseMaterial1 ="the material of the base"

#some counter on the html-page, ut makes it easier to se if somethings happens
i = 0

class MyHandler(BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
	def do_GET(s):
		# https://stackoverflow.com/questions/26563403/variables-not-updated-from-within-basehttpserver-class
		global i
		global tableHeight1,topDia1,topColor1,topMaterial1,bearingColor1,bearingMaterial1,baseColor1,baseMaterial1 #getting my global variables
		
		"""Respond to a GET request."""
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
		s.wfile.write(bytes('<html><head><style>table, th, td {border: 1px solid black;  border-collapse: collapse;}td {  padding: 5px;}</style><title>Product details.</title><form action="/product_info" method = "post"></head>', 'utf-8'))
		s.wfile.write(bytes('<body><h2>Product details</h2>' + str(i), "utf-8"))
		i = i+1

		#s.wfile.write(bytes('<form action="/product_info">', 'utf-8'))
		s.wfile.write(bytes('<br>These two figures illustrates the side view and the top view of the table. <br>Please write your desired parameters for the table below.<br><br>', 'utf-8'))
		#here comes the svg-figures
		s.wfile.write(bytes('<table style="width:30%"><tr><th>side view</th><th>top view</th></tr><tr><td><svg width="130" height="130"><rect width="120" height="10" style="fill:rgb(255,255,255);stroke-width:3;stroke:rgb(0,0,0)" /><rect x ="40" y="10" width="40" height="10" style="fill:rgb(255,255,255);stroke-width:3;stroke:rgb(0,0,0)" /><rect x ="45" y="20" width="30" height="10" style="fill:rgb(255,255,255);stroke-width:3;stroke:rgb(0,0,0)" /><rect x ="50" y="30" width="20" height="75" style="fill:rgb(255,255,255);stroke-width:3;stroke:rgb(0,0,0)" /><polygon points= 50,105,70,105,90,125,30,125 style="fill:rgb(255,255,255);stroke-width:3;stroke:rgb(0,0,0)" /></svg></td><td><svg width="130" height="130"><circle cx="65" cy="65" r="60" stroke="black" stroke-width="3" fill="white" /></svg> </td></tr></table> <br>', 'utf-8'))
		
		#the important html - user interface:		
		s.wfile.write(bytes('<label for="topDia">Diameter of the top [cm]:</label><br>', 'utf-8'))
		s.wfile.write(bytes('<input type="text" id="topDia" name="topDia" value="' + topDia1 + '"><br>', 'utf-8'))
		s.wfile.write(bytes('<label for="tableHeight">Height of the table [cm]:</label><br>', 'utf-8'))
		s.wfile.write(bytes('<input type="text" id="tableHeight" name="tableHeight" value="'+ tableHeight1 +'"><br><br>', 'utf-8'))
		s.wfile.write(bytes('<label for="topColor">Color of the top:</label><br>', 'utf-8'))
		s.wfile.write(bytes('<input type="text" id="topColor" name="topColor" value="'+ topColor1+'"><br>', 'utf-8'))
		s.wfile.write(bytes('<label for="bearingColor">Color of the bearing:</label><br>', 'utf-8'))
		s.wfile.write(bytes('<input type="text" id="bearingColor" name="bearingColor" value="'+ bearingColor1 +'"><br>', 'utf-8'))
		s.wfile.write(bytes('<label for="baseColor">Color of the base:</label><br>', 'utf-8'))
		s.wfile.write(bytes('<input type="text" id="baseColor" name="baseColor" value="'+baseColor1 +'"><br>', 'utf-8'))
		s.wfile.write(bytes('<p>To view optional colors, go to: <br> http://www.viewmold.com/ug_html_files/fusion/ug_askclosestcolor.html</p>', 'utf-8'))
		s.wfile.write(bytes('<label for="topMaterial">Material of the top:</label><br>', 'utf-8'))
		s.wfile.write(bytes('<input type="text" id="topMaterial" name="topMateial" value="'+ topMaterial1 +'"><br>', 'utf-8'))
		s.wfile.write(bytes('<label for="bearingMaterial">Material of the bearing:</label><br>', 'utf-8'))
		s.wfile.write(bytes('<input type="text" id="bearingMaterial" name="bearingMaterial" value="'+ bearingMaterial1 +'"><br>', 'utf-8'))
		s.wfile.write(bytes('<label for="baseMaterial">Material of the base:</label><br>', 'utf-8'))
		s.wfile.write(bytes('<input type="text" id="baseMaterial" name="baseMaterial" value="'+ baseMaterial1 +'"><br>', 'utf-8'))
		s.wfile.write(bytes('<p>Possible materials are:<br>Inconel 718, Titanium 6-4, C263, MSRR8670, IN939, Bronse, Silver,<br> Gold, Steel, Plastic, Oak, Wood.</p><br>', 'utf-8'))
		s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
		s.wfile.write(bytes('</form>', 'utf-8'))
		s.wfile.write(bytes('<p>If you click the "Submit" button, the form-data will be sent to a page called "/product_info".</p>', 'utf-8'))
		s.wfile.write(bytes('</body>', 'utf-8'))
		s.wfile.write(bytes('</html>', 'utf-8'))
		print("Path:", s.path)
		
	def do_POST(s):
		#https://stackoverflow.com/questions/5975952/how-to-extract-http-message-body-in-basehttprequesthandler-do-post
		
		global tableHeight1,topDia1,topColor1,topMaterial1,bearingColor1,bearingMaterial1,baseColor1,baseMaterial1
		
		#mine PARAMs
		#param = ["<topDia>", "<tableHeight>", "<topColor>", "<bearingColor>","<baseColor>","<topMaterial>","<bearingMaterial>","<baseMaterial>"]
		
		print("Path:", s.path)
		# Root path is for PARAMs update
		if s.path == "/product_info":
			s.send_response(200)
			s.send_header("Content-type", "text/html")
			s.end_headers()
			content_len = int(s.headers.get('Content-Length'))
			post_body = s.rfile.read(content_len)
			#print("Body: ", post_body.decode()) #for testing 
			"""
			# the body prints
			# topDia=120&tableHeight=90&topColor=Yellow&bearingColor=Brown&baseColor=Brown&topMateial=Oak&bearingMaterial=Oak&baseMaterial=Oak
			"""
			body_string = post_body.decode()
			key_val_pair = body_string.split('&')
			#print("key_val_pair: ", key_val_pair) #for testing
			
			# Extract params values
			p1 = key_val_pair[0].split('=')
			p2 = key_val_pair[1].split('=')
			p3 = key_val_pair[2].split('=')
			p4 = key_val_pair[3].split('=')
			p5 = key_val_pair[4].split('=')
			p6 = key_val_pair[5].split('=')
			p7 = key_val_pair[6].split('=')
			p8 = key_val_pair[7].split('=')
			
			#for testing
			#print("p1 til p7: ", p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1])

			#updating the global variables
			tableHeight1 = p2[1]
			topDia1 = p1[1]
			topColor1 = p3[1]
			bearingColor1 = p4[1]
			baseColor1 = p5[1]
			topMaterial1 =p6[1]
			bearingMaterial1 = p7[1]
			baseMaterial1 = p8[1]
			
			s.clear_fuseki() #deleting whats on fuseki 
			s.update_fuseki() #uploading to fuseki
			s.getDataFromFusekiAndMakeNewDFAFile() #getting the parameters from fuseki
			s.do_GET() #to make the web interface not freez. It is not the best way, but it works
			
	def update_fuseki(self):
		#Skal oppdatere fuseki-serveren med de parameterne jeg har
		#print("TEST update fuseki 123") #for testing
		
		URL = "http://127.0.0.1:3030/kbe/update" #getting the url
		
		global tableHeight1,topDia1,topColor1,topMaterial1,bearingColor1,bearingMaterial1,baseColor1,baseMaterial1
		
		#making the query
		#Need to change the updating parametes to parametes from the user
		query = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#> ' + \
			'PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>'+\
			'INSERT'+\
			'{'+\
			'?table kbe:hasHeight "'+ tableHeight1 +'"^^xsd:int.'+\
			'?topPlate kbe:hasDia "'+ topDia1 +'"^^xsd:int.'+\
			'?topPlate kbe:hasColor "'+ topColor1 +'"^^xsd:str.'+\
			'?topPlate kbe:hasMaterial "'+ topMaterial1 +'"^^xsd:str.'+\
			'?bearing kbe:hasColor "'+ bearingColor1 +'"^^xsd:str.'+\
			'?bearing kbe:hasMaterial "'+ bearingMaterial1 +'"^^xsd:str.'+\
			'?base kbe:hasColor "'+baseColor1 +'"^^xsd:str.'+\
			'?base kbe:hasMaterial "'+ baseMaterial1 +'"^^xsd:str.'+\
			'}'+\
			'WHERE'+\
			'{'+\
			'?table a kbe:Table.'+\
			'?topPlate a kbe:TopPlate.'+\
			'?bearing a kbe:Bearing.'+\
			'?base a kbe:Base.'+\
			'}'
		# defining a query params 
		PARAMS = {'update': query} 
		r = requests.post(url = URL, data = PARAMS)
		#Checking the result
		print("Result of INSERT query:", r.text)
		
	def getDataFromFusekiAndMakeNewDFAFile(self):
		#this function connects to the fuseki server and get whats on it and makes a new file for the parameters based on the template
		#Get in contact with fuseki
		URL = "http://127.0.0.1:3030/kbe/query"
		
		# defining a query params 
		PARAMS = {'query': 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>\
					SELECT ?topDia ?height ?topCol ?bearingCol ?baseCol ?topMat ?bearingMat ?baseMat\
					WHERE\
					{\
					?topPlate a kbe:TopPlate.\
					?topPlate kbe:hasDia ?topDia.\
					?topPlate kbe:hasColor ?topCol.\
					?topPlate kbe:hasMaterial ?topMat.\
					?table a kbe:Table.\
					?table kbe:hasHeight ?height.\
					?bearing a kbe:Bearing.\
					?bearing kbe:hasColor ?bearingCol.\
					?bearing kbe:hasMaterial ?bearingMat.\
					?base a kbe:Base.\
					?base kbe:hasColor ?baseCol.\
					?base kbe:hasMaterial ?baseMat.\
					}'} 
		# sending get request and saving the response as response object 
		r = requests.get(url = URL, params = PARAMS)
		data = r.json()
		#print("JSON:", data) #for testing
		"""
		If I am able to store several tables on the fuseki server, without mess, 
		this must be double cheched so that the right values for the latest table get picked out. 
		"""
		# need to get the parameter values out of the "data"
		sides = [data['results']['bindings'][0]['topDia']['value'],\
				data['results']['bindings'][0]['height']['value'],\
				data['results']['bindings'][0]['topCol']['value'],\
				data['results']['bindings'][0]['bearingCol']['value'],\
				data['results']['bindings'][0]['baseCol']['value'],\
				data['results']['bindings'][0]['topMat']['value'],\
				data['results']['bindings'][0]['bearingMat']['value'],\
				data['results']['bindings'][0]['baseMat']['value']]
		#print("sides", sides)
		newparam = sides
		print("newparam: ", newparam) #only for testing
		#parameternames in the template-dfa.
		param = ["<topDia>", "<tableHeight>", "<topColor>", "<bearingColor>","<baseColor>","<topMaterial>","<bearingMaterial>","<baseMaterial>"]
		
		#Reading the template file
		f = open(PATH_TO_DFA + "templates\\" + DFA_TEMPLATE_FILE_NAME, "r")
		tekst = f.read() #legger teksten til en streng

		#replace for param 
		for i in range(len(param)):
			tekst = tekst.replace(param[i],newparam[i])	
		tekst = tekst.replace("<table_template>", NEW_DFA_FILE_NAME) #change the class name for the new file, needed to be opened in nx
		f.close

		##need to change the file-path
		#writing to the right location
		f = open(PATH_TO_DFA + NEW_DFA_FILE_NAME, "w") #åpner skrivetilgang, ønsker å skrive over det som står i dokumentet
		f.write(tekst) #legger til den nye teksten
		f.close() #lukker fila
		print("Redy to open ",  NEW_DFA_FILE_NAME)
		"""
		If there were several tables, 
		the new file name should be extended with a iterable value, 
		so that each order gets its own file.
		"""
		
	def clear_fuseki(self):  
			#This function deletes everything 
			#for testing
			#print("test clear fuseki 123")
			URL = "http://127.0.0.1:3030/kbe/update" #get the url 
			"""
			Use of POST with requests module:
			https://www.w3schools.com/python/ref_requests_post.asp
			"""
			
			#I want to delete every value of each object
			""" What Andrei suggested and did not work for me 
			query = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>'+\
					'PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>'+\
					'DELETE'+\
					'{'+\
					'kbe:table a kbe:Table.'+\
					'kbe:table ?pred ?obj.'+\
					'kbe:topPlate a kbe:TopPlate.'+\
					'kbe:topPlate ?pred ?obj.'+\
					'kbe:bearing a kbe:Bearing.'+\
					'kbe:bearing ?pred ?obj.'+\
					'kbe:base a kbe:Base.'+\
					'kbe:base ?pred ?obj.'+\
					'}'+\
					'WHERE'+\
					'{'+\
					'kbe:table ?pred ?obj.'+\
					'kbe:topPlate ?pred ?obj.'+\
					'kbe:bearing ?pred ?obj.'+\
					'kbe:base ?pred ?obj.'+\
					'}'
				"""
			#this might give som problem if one of the properties does not exist befor I try to delete it
			query = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#> '+\
					'DELETE'+\
					'{'+\
					'?topPlate kbe:hasDia ?topDia.'+\
					'?topPlate kbe:hasColor ?topCol.'+\
					'?topPlate kbe:hasMaterial ?topMat.'+\
					'?table kbe:hasHeight ?height.'+\
					'?bearing kbe:hasColor ?bearingCol.'+\
					'?bearing kbe:hasMaterial ?bearingMat.'+\
					'?base kbe:hasColor ?baseCol.'+\
					'?base kbe:hasMaterial ?baseMat.'+\
					'}'+\
					'WHERE'+\
					'{'+\
					'?topPlate kbe:hasDia ?topDia.'+\
					'?topPlate kbe:hasColor ?topCol.'+\
					'?topPlate kbe:hasMaterial ?topMat.'+\
					'?table kbe:hasHeight ?height.'+\
					'?bearing kbe:hasColor ?bearingCol.'+\
					'?bearing kbe:hasMaterial ?bearingMat.'+\
					'?base kbe:hasColor ?baseCol.'+\
					'?base kbe:hasMaterial ?baseMat.'+\
					'}'
			# defining a query params 
			PARAMS = {'update': query} 
			# sending get request and saving the response as response object 
			r = requests.post(url = URL, data = PARAMS) 
			#Checking the result
			print("Result:", r.text)
	
 
if __name__ == '__main__':
	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
