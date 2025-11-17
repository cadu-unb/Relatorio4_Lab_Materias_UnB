import matplotlib.pyplot as plt
import numpy as np # Importado para ajudar na manipulação do eixo x

# ----------------- DADOS CORRIGIDOS E RESOLUÇÃO DE DUPLICATAS -----------------
# Baseado na sua lista de tensão (16 pontos), ajustamos a corrente para 16 pontos.
# Tensões: [-0.8, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.77]
# Correntes (Assumindo 0 para as tensões negativas/baixas):
tensao_v = [-0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.77]
corrente_ma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.7, 3.3, 29.7, 30.4] # 16 pontos

# Criação da figura
plt.figure(figsize=(10, 5)) # Aumentei o tamanho da figura para melhor visualização

# Plotagem dos dados
plt.plot(tensao_v, corrente_ma, marker='o', linestyle='-', color='red')

# 1. Configuração do Título com afastamento (y=1.05 move para cima)
plt.title(r'$I_D\times V_D$', fontsize=20, y=1.05)

# 2. Garantir que todos os pontos de X sejam exibidos como "ticks"
# Removemos a necessidade do numpy, plotamos apenas os valores de tensão originais.
plt.xticks(tensao_v, rotation=45, ha='right') # Rotaciona para evitar sobreposição

# Rótulos dos Eixos
plt.xlabel('Tensão [V]', fontsize=16)
plt.ylabel('Corrente [mA]', fontsize=16)

# Adiciona grade
plt.grid(True, linestyle='--', alpha=0.6)

# Ajusta o layout para acomodar os rótulos rotacionados e o título afastado
plt.tight_layout()

# 3. Salvar o gráfico em PDF e PNG (300 dpi)
file_name_png = 'grafico_ID_x_VD.png'
file_name_pdf = 'grafico_ID_x_VD.pdf'

plt.savefig(file_name_png, dpi=300)
plt.savefig(file_name_pdf, dpi=300) # Salva o PDF com 300 dpi (alta qualidade)

plt.show() # Usado apenas para fins de visualização no ambiente de execução