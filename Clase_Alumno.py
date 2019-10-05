class Alumno():
	def __init__(self, nombre, apellido):
		self.nombre=nombre
		self.apellido=apellido
		self.marticula=True
		self.inactivo=True
		self.graduar=True

	def matriculado(self, matriculados):
		self.matricula=matriculados
		if(self.matricula):
			print("el alumno esta matriculado")
		else:
			print("alumno esta inhabilitado o graduado")


	def inhabilitado(self, inhabilitados):
		self.inactivo=inhabilitados
		if(self.inactivo):
			print("el alumno esta inhabilitado")
		else:
			print("el alumno esta matriculado")

	def graduado(self, graduados):
		self.graduar=graduados
		if(self.graduar):
			print("el alumno esta graduado")
		else:
			print("el alumno esta matriculado y activo")
		
    





carlos=Alumno("Carlos","Garcia")
carlos.matriculado(True)
carlos.inhabilitado(False)
carlos.graduado(False)


