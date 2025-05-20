# Element Detector in Binary Images

Este projeto tem como objetivo detectar elementos, como estrelas, em imagens binárias. Ele utiliza as bibliotecas OpenCV, NumPy, Scikit-Image e Matplotlib para realizar o processamento das imagens.

## Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

```
element-detector-in-binary-images/
├── README.md                 # Este arquivo, com informações e instruções.
├── requirements.txt          # Dependências do projeto.
├── data/                     # Pasta de dados para as imagens.
│   └── imagem_meteoro.png    # Exemplo de imagem para processamento.
└── src/                      # Código fonte do projeto.
    └── countElements.py      # Script principal de detecção de elementos.
```

## Pré-Requisitos

- [Python 3.x](https://www.python.org/downloads/)
- Pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório ou faça o download dos arquivos do projeto.
2. Navegue até a pasta raiz do projeto.
3. Instale as dependências executando o comando:

   ```sh
   python -m pip install -r requirements.txt
   ```

## Como Executar o Projeto

Para rodar o script principal (`countElements.py`), execute o comando abaixo na raiz do projeto:

```sh
python -m src.countElements
```

Se configurado corretamente, o script irá:
- Carregar a imagem da pasta `data`.
- Processar a imagem para identificar elementos (estrelas).
- Exibir a imagem original e a processada com a detecção realizada.

## Como o Código Funciona

O script em `src/countElements.py` segue os seguintes passos:

- **Carregamento da Imagem:**  
  Utiliza `cv2.imread` para carregar a imagem a partir da pasta `data`. Caso a imagem não seja carregada corretamente, exibe uma mensagem de erro.

- **Processamento da Imagem:**  
  Se a imagem for carregada com sucesso, ela é convertida de BGR (formato padrão do OpenCV) para RGB, que é mais adequado para visualização com Matplotlib. Em seguida, cria uma máscara para identificar os pixels que são praticamente brancos, correspondendo aos elementos de interesse (por exemplo, estrelas).

- **Detecção de Elementos:**  
  A função `measure.label` (do Scikit-Image) é utilizada para rotular as regiões conectadas na imagem binária. O número máximo de rótulos encontrados representa a quantidade de elementos detectados.

- **Exibição dos Resultados:**  
  Por fim, o script exibe duas imagens lado a lado: a imagem original e a imagem processada, facilitando a visualização dos elementos detectados.

## Executando Testes

Se você deseja rodar os testes unitários, certifique-se de que o pytest está instalado e execute:

```sh
pytest
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

