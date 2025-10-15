carro = {
    "marca": "chevrolet",
    "modelo": "onix",
    "ano":"2020"

}    

print(carro["marca"])

carro['cor'] = 'preto'

carro.update({"ano": 2025})

carro.pop("modelo")

print(carro.get("tamanho"))

carro.keys()

print(carro.keys())

carro.values()

print(carro.values())

carro.items()

print(carro.items()) 

for chave, valor in carro.items():
    print(chave ," ", valor)