# Calculadora de Horas Trabalhadas com Cronômetro

Este é um aplicativo desktop simples desenvolvido em Python usando a biblioteca **Tkinter**, que permite calcular o total de horas trabalhadas com base em uma hora inicial e um cronômetro embutido. O programa também permite exportar os dados calculados para uma planilha Excel.

## Funcionalidades

- **Registro Automático da Hora Inicial**: A hora inicial é capturada automaticamente ao iniciar o cronômetro.
- **Cronômetro Visual**: Exibe o tempo decorrido em tempo real enquanto o cronômetro está em andamento.
- **Cálculo de Horas Trabalhadas**: Calcula automaticamente as horas trabalhadas ao parar o cronômetro.
- **Exportação para Excel**: Exporta os dados registrados para um arquivo Excel, permitindo fácil consulta e análise.
- **Interface Amigável**: Interface gráfica simples e intuitiva para facilitar o uso.
- **Janela Fixa**: O tamanho da janela não pode ser redimensionado, garantindo uma experiência mais consistente.

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada no projeto.
- **Tkinter**: Biblioteca padrão do Python para a criação de interfaces gráficas.
- **Pandas**: Utilizada para manipulação de dados e geração da planilha Excel.
- **OpenPyXL**: Motor para salvar os dados no formato Excel.

## Como Usar

1. **Instale os Requisitos**:
   Certifique-se de que você tem o Python instalado em seu sistema. Instale as dependências com o seguinte comando:
   ```bash
   pip install pandas openpyxl
   ```

2. **Execute o Programa**:
   Execute o script `calculadora_horas.py`:
   ```bash
   python calculadora_horas.py
   ```

3. **Utilize a Interface**:
   - Insira o número do ticket no campo correspondente.
   - Clique em "Iniciar Cronômetro" para capturar a hora inicial.
   - Clique em "Parar Cronômetro" para registrar o tempo decorrido.
   - Clique em "Calcular Horas" para registrar as horas trabalhadas.
   - Clique em "Exportar para Planilha" para salvar os dados em um arquivo Excel.

4. **Acesse os Dados**:
   Os dados exportados serão salvos em um arquivo chamado `horas_tickets.xlsx` no diretório do programa.

## Estrutura do Projeto

```
.
├── calculadora_horas.py  # Código principal do aplicativo
├── horas_tickets.xlsx    # Arquivo gerado com os dados (após exportação)
└── README.md             # Documentação do projeto
```

## Captura de Tela

(Adicione aqui uma captura de tela do aplicativo em execução para ilustrar a interface gráfica.)

## Melhorias Futuras

- Adicionar funcionalidade para editar ou excluir entradas diretamente pela interface.
- Permitir personalização do formato de exportação (e.g., CSV).
- Adicionar suporte para múltiplos idiomas.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com sugestões e melhorias.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

Feito com 💻 e ☕ por [Seu Nome](https://github.com/seuusuario).

