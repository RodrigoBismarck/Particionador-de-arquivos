with open("C:\\Users\\rodrigo.araujo\\Documents\\dados.txt","r") as arquivo: #Define o caminho do arquivo que será particionado
    linha = 0
    versao = 0
    informacoes = []
    while True:
        registro = arquivo.readline()
        informacoes.append(registro)
        linha+=1
        if len(informacoes)<=1000: #Define em quantas linhas deseja particionar o arquivo, neste caso 1000
            continue
        else:
            with open(f"C:\\Users\\rodrigo.araujo\\Documents\\dados{versao}.txt","w") as file: #Define o caminho das partições do arquivo
                for i in informacoes:
                    file.write(i)
                informacoes.clear()
                versao+=1
                print(versao)
                if len(registro) == 0:
                    break
                


