# Conversor de Caso de Texto

Este projeto é um simples conversor de texto que permite ao usuário transformar strings digitadas em diferentes formatos: MAIÚSCULAS, minúsculas e Capitalizadas (título). O aplicativo é desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica.

## Funcionalidades

- **Conversão para MAIÚSCULAS**: Converte todo o texto inserido para letras maiúsculas.
- **Conversão para minúsculas**: Converte todo o texto inserido para letras minúsculas.
- **Capitalização**: Converte a primeira letra do texto inserido para maiúscula, mantendo o restante em minúsculas.
- **Interface gráfica**: Uma interface amigável e simples para interação do usuário.

## Como Usar

O executável do conversor de texto está disponível na pasta `dist` deste repositório. Para executar o programa:

1. Baixe o arquivo executável `conversor_caso.exe` da pasta `dist`.
2. Execute o arquivo diretamente em seu sistema operacional.

Se preferir rodar o código-fonte:

1. Clone este repositório em sua máquina local.
2. Certifique-se de ter o Python instalado.
3. Instale as dependências (se houver) utilizando `pip install -r requirements.txt` (caso você tenha um arquivo de requisitos).
4. Execute o arquivo `conversor_caso.py` para iniciar o aplicativo.

## Empacotamento

O programa também pode ser convertido em um arquivo executável (.exe) utilizando o PyInstaller. Para isso, utilize o comando:

```bash
pyinstaller --onefile --windowed conversor_caso.py
```

O executável gerado estará na pasta `dist`.

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. 

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
