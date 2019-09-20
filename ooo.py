s=int(input('Si eres hombre pon 0, si eres mujer pon 1: ')) 
a=True
while a:

	if s==0:
		x=26662
		a=False
	elif s==1:
		x=28854
		a=False
	else:
		s=int(input('Que pongas un 1 o un 0: '))

print('Ingresa tu fecha de nacimiento')
a=int(input('Año de nacimiento: '))
m=int(input('Mes de nacimiento: '))
d=int(input('Dia de nacimiento: '))



from datetime import date

c=date(a,m,d)

def vida(c):
	h = date.today()
	return abs(h - c).days

muerte=x-(vida(c))

print('.'*(vida(c)), '-'*(muerte))

print(f'Has vivido {vida(c)} días y estadísticamente te quedan {muerte} días de vida')