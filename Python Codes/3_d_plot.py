import matplotlib.pyplot as plt

# 1. Configuração dos vértices (Projeção em perspectiva oblíqua)
A = (0, 1)
D = (4, 1)
D_prime = (4, 0)
A_prime = (0, 0)

# Deslocamento de profundidade para a face traseira
dx, dy = 1.2, 0.6
B = (A[0] + dx, A[1] + dy)
C = (D[0] + dx, D[1] + dy)
C_prime = (D_prime[0] + dx, D_prime[1] + dy)
B_prime = (A_prime[0] + dx, A_prime[1] + dy)

# 2. Configuração da figura
fig, ax = plt.subplots(figsize=(12, 8))

# 3. Desenhando as arestas visíveis (Sólidas)
# Face superior
ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', lw=1.5)
ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', lw=1.5)
ax.plot([C[0], D[0]], [C[1], D[1]], 'k-', lw=1.5)
ax.plot([D[0], A[0]], [D[1], A[1]], 'k-', lw=1.5)

# Arestas verticais visíveis
ax.plot([A[0], A_prime[0]], [A[1], A_prime[1]], 'k-', lw=1.5)
ax.plot([D[0], D_prime[0]], [D[1], D_prime[1]], 'k-', lw=1.5)
ax.plot([C[0], C_prime[0]], [C[1], C_prime[1]], 'k-', lw=1.5)

# Arestas da base visíveis
ax.plot([A_prime[0], D_prime[0]], [A_prime[1], D_prime[1]], 'k-', lw=1.5)
ax.plot([D_prime[0], C_prime[0]], [D_prime[1], C_prime[1]], 'k-', lw=1.5)

# 4. Desenhando as arestas ocultas (Tracejadas)
ax.plot([B[0], B_prime[0]], [B[1], B_prime[1]], 'k--', lw=1.5)
ax.plot([A_prime[0], B_prime[0]], [A_prime[1], B_prime[1]], 'k--', lw=1.5)
ax.plot([B_prime[0], C_prime[0]], [B_prime[1], C_prime[1]], 'k--', lw=1.5)

# 5. Adicionando os Rótulos (Labels)
offset = 0.15
fontsize = 16

# Topo
ax.text(A[0] - offset, A[1] + offset/3, 'A', fontsize=fontsize, ha='right')
ax.text(B[0] - offset/2, B[1] + offset/2, 'B', fontsize=fontsize, ha='center')
ax.text(C[0] + offset, C[1] + offset/2, 'C', fontsize=fontsize, ha='center')
ax.text(D[0] - offset, D[1] + offset/3, 'D', fontsize=fontsize, ha='right')

# Base
ax.text(A_prime[0] - offset, A_prime[1] - offset, "A'", fontsize=fontsize, ha='right')
ax.text(B_prime[0] + offset, B_prime[1] + offset/2, "B'", fontsize=fontsize, ha='left')
ax.text(C_prime[0] + offset, C_prime[1] - offset, "C'", fontsize=fontsize, ha='left')
ax.text(D_prime[0] + offset/2, D_prime[1] - offset, "D'", fontsize=fontsize, ha='center')

# 6. Limpeza e Exportação
ax.set_aspect('equal')
ax.axis('off') # Remove os eixos do gráfico

plt.tight_layout()

# Salva o arquivo SVG com fundo transparente para o Quarto
plt.savefig('dominio_fundamental.svg', format='svg', transparent=True)
print("Arquivo 'dominio_fundamental.svg' gerado com sucesso!")