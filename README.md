
# Relatório 4 — Lab. Materiais Magnéticos e Elétricos (UnB)

Este repositório contém o código, imagens e fontes LaTeX usadas para montar o relatório final (arquivo principal `r4.tex`).

## Problemas atuais:

Tudo...

## Instruções Gerais:

* Para visualizar o resultado atual do trabalho abra o arquivo "r4.pdf" que pode ser encontrado na pasta raiz desse repostiório.

* Para realizar alterações será necessário criar um conta no GitHub e solicitar ao administrador do reposítorio que lhê adicione a equipe de desenvolvimento.

* As eventuais alterações devem ser realizadas no arquivo "r4.tex" utilizando a linguagem LaTex.

* Para "plotar" os gráficos será utilizada a biblioteca MatPlotLib do Python3.

* Em caso de dúvidas sobre sintaxe, forma e afins o Gemini ou o GPT saberão explicar melhor que eu.

## Como rodar LaTex pelo VSCODE? - Windowns 10-11:

1. Baixe/instale o VSCODE - [link](https://code.visualstudio.com/download);
2. Baixe/instale o Git - [link](https://git-scm.com/downloads);
3. Baixe/instale Miktech - [link](https://miktex.org/download);
4. Baixe/instale Strawberry Perl - [link](https://strawberryperl.com/);

**Estrutura de arquivos**
- **`r4.tex`**: Arquivo principal do relatório — chama os outros arquivos `.tex` com `\input{...}`.
- **Partes do relatório**: `r4-intro.tex`, `r4-materiais.tex`, `r4-objetivos.tex`, `r4-procedimentos.tex`, `r4-resultados.tex`, `r4-conclusoes.tex`, `r4-apendice-script.tex` (cada uma contém um capítulo/seção específica).
- **Estilos e bibliografia**: `cvpr.sty`, `cvpr_eso.sty`, `cor.tex`, `ieee_fullname.bst`, `egbib.bib`, `r4.bbl`.
- **Imagens**: pastas `fotos/`, `imagens/` e `imagens/PNG/` (conteúdo usado nas figuras do relatório).
- **Scripts úteis**: `reduce_image_sizes.py` (reduz tamanho de imagens), `graphcs.py` (scripts de plotagem) e `reduce_image_sizes.py`.

**Como o `r4.tex` monta o documento**
- **Inclusão de sub-arquivos**: o `r4.tex` usa comandos `\input{r4-intro.tex}` (ou caminhos relativos) para inserir o conteúdo dos capítulos. Isso mantém cada parte em arquivos separados e facilita edição colaborativa.
- **Fluxo típico**: editar os arquivos `.tex` individuais → compilar `r4.tex` → revisar `r4.pdf`.

**Compilação (exemplos)**
- **Recomendado (latexmk)**: `latexmk -pdf r4.tex` — compila e resolve referências automaticamente.
- **Alternativa com pdflatex/bibtex** (manual):
	- `pdflatex r4.tex`
	- `bibtex r4` (se necessário)
	- `pdflatex r4.tex`
	- `pdflatex r4.tex`
- **VS Code (preferencial)**: instale a extensão LaTeX Workshop e abra `r4.tex`; ou use sua distribuição TeX (MiKTeX/TeX Live) no Windows.

**Reduzir o tamanho das imagens**
O repositório inclui o script `reduce_image_sizes.py` que facilita reduzir o tamanho das imagens (útil antes de subir para o Overleaf ou para diminuir o PDF final):

- **O que o script faz**: percorre a árvore de diretórios a partir da pasta onde o script está localizado, detecta imagens (`.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.tiff`) e gera uma versão reduzida chamada `reduced_<nome_original>` no mesmo diretório. O alvo padrão é ~250 KB; o script tenta primeiro reduzir qualidade (JPEG/WEBP) e depois reduzir resolução quando necessário.
- **Requisitos**: Python 3.x e a biblioteca Pillow. Para instalar Pillow execute:

```powershell
pip install --user pillow
```

- **Como executar (PowerShell)**: posicione-se na raiz do repositório (onde está `reduce_image_sizes.py`) e rode:

```powershell
# usando python disponível no PATH
python .\reduce_image_sizes.py

# ou, se precisar do caminho completo do executável Python (exemplo):
& 'C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python313\python.exe' 'D:\Google Drive\9-2aGraduacao-UnB\Eng. Eletrica\LabMatMagEl\Relatorio4_Lab_Materias_UnB\reduce_image_sizes.py'
```

- **O que procurar depois**: o script criará arquivos com prefixo `reduced_` — ex.: `reduced_figura1.png`. Verifique visualmente cada `reduced_...` antes de substituir o original.

- **Substituir arquivos originais (opcional e com backup recomendado)**: se você revisar os `reduced_` e quiser trocar os originais automaticamente, faça um backup antes. Um comando PowerShell para listar os novos arquivos:

```powershell
Get-ChildItem -Recurse -Filter "reduced_*"
```

Para substituir automaticamente (EXEMPLO — faça backup antes):

```powershell
# Atenção: executa substituição em lote. Faça commit/backup antes de rodar.
Get-ChildItem -Recurse -Filter "reduced_*" | ForEach-Object {
	$reduced = $_.FullName
	$original = $reduced -replace '\\reduced_', '\\'
	Move-Item -Force $reduced $original
}
```

Observação: revise o comando acima antes de executar — caminhos e backups são responsabilidade do usuário.

**Boas práticas**
- **Verifique visualmente** os `reduced_...` antes de substituir os originais; alguns detalhes finos podem ser perdidos com compressão muito agressiva.
- **Organização**: você pode manter imagens otimizadas em `imagens/optimized/` e referenciar essas versões no `.tex` até validar o resultado.
- **Controle de versão**: evite commitar imagens muito grandes no repositório; prefira versões reduzidas ou um repositório separado para dados brutos.

**Próximos passos sugeridos**
- Se quiser, eu posso rodar o `reduce_image_sizes.py` aqui e listar os `reduced_` gerados para revisão.
- Posso também ajudar a criar um script que substitua somente arquivos que passem num threshold visual (por ex. tamanho e resolução) com segurança.