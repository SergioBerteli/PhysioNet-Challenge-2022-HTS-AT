# Identificador de presença de sopro cardíaco

Este repositório contém o código desenvolvido como Trabalho de Conclusão de Curso (TCC) do curso de Engenharia de Computação. O objetivo do projeto é identificar a presença de sopro cardíaco em fonocardiogramas (FCGs), classificando cada registro como: "presente", "ausente" ou "incerto".

Para o treinamento e avaliação foi utilizada a base de dados The CirCor DigiScope Phonocardiogram Dataset (v1.0.3), disponível em: https://physionet.org/content/circor-heart-sound/1.0.3/.

Arquitetura: A arquitetura adotada é o HTS-AT, um Transformer hierárquico com mecanismo de atenção por janelas projetado para tarefas de classificação de áudio.

Autor: Sergio Berteli Batista Filho

## Guia para treinar o modelo

1. Requisitos iniciais
   - Baixe a base de dados The CirCor DigiScope Phonocardiogram Dataset a partir do PhysioNet (link acima) e organize os arquivos conforme exigido pelo notebook. O notebook inclui células iniciais que apresentam o formato de entrada esperado — verifique-as para ajustar a estrutura de diretórios e nomes de arquivos.
   - Se preferir utilizar a base já dividida usada neste trabalho, ela está disponível neste link: https://drive.google.com/file/d/1SRA5okbjchFDET2zu3rzuHlYAA5oas4I/view.

2. Notebook principal
   - O notebook de treinamento e avaliação é: TCC_sopro_V2.ipynb
   - Todas as etapas do fluxo (criação de pastas, pré-processamento básico, treinamento, validação, teste e salvamento do(s) modelo(s)) estão implementadas nesse notebook.

3. Execução em Google Colab
   - O notebook foi originalmente desenvolvido para execução no Google Colab e utiliza o Google Drive para armazenar conjuntos de dados, checkpoints e resultados.
   - Para executar no Colab, monte o Google Drive e ajuste os caminhos conforme as instruções nas primeiras células do notebook.

4. Execução local
   - Para rodar localmente, serão necessárias adaptações:
     - Ajustar caminhos de leitura/escrita.
     - Verificar disponibilidade de GPU e compatibilidade da versão do CUDA/cuDNN com os pacotes instalados.
     - Garantir que o ambiente Python e as dependências estejam corretamente instalados.


## Instalação de dependências para execução local

Recomenda-se criar um ambiente isolado antes de instalar as dependências:

```bash
conda create -n myenv python=3.12 -y
conda activate myenv
```

Em seguida, instale os pacotes listados no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

```bash
jupyter notebook
```


## Links úteis
- Dataset (PhysioNet): https://physionet.org/content/circor-heart-sound/1.0.3/
- Conjunto pré-processado utilizado no trabalho: https://drive.google.com/file/d/1SRA5okbjchFDET2zu3rzuHlYAA5oas4I/view
- Relatório / Trabalho desenvolvido: https://drive.google.com/file/d/1J2OnJVaBgXhy45cO_Um29khuvGvOoHrP/view?usp=sharing

