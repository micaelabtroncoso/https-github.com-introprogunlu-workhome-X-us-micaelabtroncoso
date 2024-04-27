def area_perimetro_rectangulo(base, altura):
   
    """Esta funcion recibe la altura y devuelve el area"""
   
    perimetro = 0
    area = 0
    area = base*altura
    perimetro= base*2 + altura*2
    return perimetro,area

x = int (input("base:"))
y = int (input("altura:"))


p, a = area_perimetro_rectangulo(x,y) 

print("El perimetro es" + str(p))
print("El area es"+ str(a))
