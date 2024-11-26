import os
import glob

def buscar_arquivos(diretorio, extensoes):
    arquivos_encontrados = []
    for ext in extensoes:
        arquivos_encontrados.extend(glob.glob(os.path.join(diretorio, '**', '*' + ext), recursive=True))
    return arquivos_encontrados

def gerar_relatorio(arquivos):
    if arquivos:
        with open('relatorio.txt', 'w') as f:
            for arquivo in arquivos:
                f.write(arquivo + '\n')
        print(f'Relatório gerado com {len(arquivos)} arquivos encontrados.')
    else:
        print('Nenhum arquivo encontrado.')

def main():
    diretorio_inicial = input("Informe o diretório para buscar os arquivos: ").replace("\\", "/")
    
    if not os.path.isdir(diretorio_inicial):
        print("O diretório informado não existe ou não é válido.")
        return
    
    extensoes = ['.exe', '.bat']  
    
    arquivos = buscar_arquivos(diretorio_inicial, extensoes)
    
    gerar_relatorio(arquivos)

    if arquivos:
        print(f"Arquivos encontrados: {len(arquivos)}")
        for arquivo in arquivos:
            print(arquivo)
    else:
        print("Nenhum arquivo encontrado.")

if __name__ == "__main__":
    main()
