estoque = {

"maça": "5" ,
"banana": "6" ,
"uva": "10"

}

estoque.update({'maça': 7})

estoque['pera'] = 8

del estoque['banana']

estoque.clear()

print(estoque)