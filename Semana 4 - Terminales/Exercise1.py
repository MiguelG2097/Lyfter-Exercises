name = input("Ingrese su nombre")
lastname = input("Ingrese su apellido")
age = int(input("Ingrese su edad"))

if age <= 2:
    life_stage = "bebe"
elif age <= 7:
    life_stage = "niño"
elif age <= 12:
    life_stage = "preadolescente"
elif age <= 17:
    life_stage = "adolescente"
elif age <= 25:
    life_stage = "adulto joven"
elif age <= 59:
    life_stage = "adulto"
else:
    life_stage = "adulto mayor"

print(f"{name} {lastname}, tienes {age} años y eres: {life_stage}")

