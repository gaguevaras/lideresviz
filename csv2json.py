import csv  
import json  
  
# Open the CSV  
f = open( 'events.csv', 'rU' )  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ("id","Nombre","datasketch","pacifista","ojoalapaz","indepaz","ONU","Defensoria","Unidad de Victimas","Somos Defensores","Cinep. Noche y Niebla","CODHES","Colectivo de Abogados José Alvear Restrepo Cajar","Género","Fecha","Municipio","Departamento","Tipo de líder","Cargo","Móvil","Otros","Fuentes"))  
# Parse the CSV into JSON  
out = json.dumps( [ row for row in reader ] )  
print ("JSON parsed!")
# Save the JSON  
f = open( 'events.json', 'w')  
f.write(out)  
print ("JSON saved!")
