s.wfile.write(bytes("<!DOCTYPE html><html><body>", 'utf-8'))
s.wfile.write(bytes("<h2>Product details intervals and available</h2>", 'utf-8'))
s.wfile.write(bytes("<p>Please fill in details about the production below. </p>", 'utf-8'))

s.wfile.write(bytes("<form action="/action_page.php">", 'utf-8'))

#intervals for leg length, leg side, seat side, back height
s.wfile.write(bytes("<p> Write maximum and minimum parameters. </p>", 'utf-8'))

s.wfile.write(bytes('<label for="leg_lengthUp">Max leg length:</label><br>', 'utf-8'))
s.wfile.write(bytes('<input type="text" id="leg_lengthUp" name="leg_lengthUp" value="John"><br>', 'utf-8'))
s.wfile.write(bytes('<label for="leg_lengthLow">Min leg length:</label><br>', 'utf-8'))
s.wfile.write(bytes('<input type="text" id="leg_lengthLow" name="leg_lengthLow" value="Doe"><br><br>', 'utf-8'))

s.wfile.write(bytes('<label for="leg_sideUp">Max leg width:</label><br>', 'utf-8'))
s.wfile.write(bytes('<input type="text" id="leg_sideUp" name="leg_sideUp" value="John"><br>', 'utf-8'))
s.wfile.write(bytes('<label for="leg_sideLow">Min leg width:</label><br>', 'utf-8'))
s.wfile.write(bytes('<input type="text" id="leg_sideLow" name="leg_sideLow" value="Doe"><br><br>', 'utf-8'))

s.wfile.write(bytes('<label for="seat_sideUp">Max seat width:</label><br>', 'utf-8'))
s.wfile.write(bytes('<input type="text" id="seat_sideUp" name="seat_sideUp" value="John"><br>', 'utf-8'))
s.wfile.write(bytes('<label for="seat_sideLow">Min seat width:</label><br>', 'utf-8'))
s.wfile.write(bytes('<input type="text" id="seat_sideLow" name="seat_sideLow" value="Doe"><br><br>', 'utf-8'))

s.wfile.write(bytes('<label for="back_heightUp">Max back height:</label><br>', 'utf-8'))
s.wfile.write(bytes('<input type="text" id="back_heightUp" name="back_heightUp" value="John"><br>', 'utf-8'))
s.wfile.write(bytes('<label for="back_heightLow">Min back height:</label><br>', 'utf-8'))
s.wfile.write(bytes('<input type="text" id="back_heightLow" name="back_heightLow" value="Doe"><br><br>', 'utf-8'))

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


  
  
  
  
  
  
 

