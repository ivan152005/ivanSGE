dbname='postgres'
user='postgres'
password='root'
host='localhost'
port='5432'


query1 = """SELECT p.id, p.nombre, p.apellidos, p.edad, p.fechanacimiento, p.estado, p.fechadefuncion, p.iddireccion
	FROM scexamen.personas p
	WHERE p.estado = 1;"""

query1_1 = """SELECT v.idCiudadOrigen, v.idCiudadDestino
	FROM scexamen.vuelos v JOIN scexamen.usuariosvuelo u
	ON v.id = u.idVuelo JOIN scexamen.personas p
	ON p.id = u.idPasajero
	WHERE p.estado = 1 and p.id = :id;"""

query2 = """SELECT p.nombre, d.calle, d.cp
	FROM scexamen.personas p JOIN scexamen.direccion d
	ON p.iddireccion = d.id
	WHERE p.estado = 1 and p.id = :id;"""

query3 = """SELECT p.nombre, p.apellidos, c.nombre, c2.nombre, u.precioBillete
	FROM scexamen.vuelos v JOIN scexamen.usuariosvuelo u
	ON v.id = u.idVuelo JOIN scexamen.personas p
	ON p.id = u.idPasajero JOIN scexamen.Ciudades c
	ON c.id = v.idCiudadOrigen JOIN scexamen.Ciudades c2
	ON c2.id = v.idCiudadDestino
	WHERE p.estado = 1;"""

query4 = """UPDATE scexamen.vuelos
	SET estadovuelo='No Destino', fechavuelo= CURRENT_DATE
	WHERE id = 5 or id = 7;"""