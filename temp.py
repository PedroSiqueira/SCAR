def func(index):
    try:
        if index==0:
            raise Exception('tentando novamente')
        else:
            print("fim")
    except Exception as e:
        print('Erro: ' + str(e))
        if input("Deseja tentar novamente? (s/n) ").lower()=='s':
            func(index)

print(input("Deseja tentar novamente? (s/n) ").lower())
func(0)
