import matplotlib.pyplot as plt

# 1. Configuração dos vértices do Hexágono Superior (Projeção Afim)
# Os vetores foram escolhidos para manter paralelismo estrito entre arestas opostas
A = (0, 3.5)
B = (2.0, 5.0)
C = (5.5, 5.0)
D = (7.0, 3.0)
E = (5.0, 1.5)
F = (1.5, 1.5)

# 2. Configuração dos vértices do Hexágono Inferior (Deslocamento vertical)
dy = -3.0
A_prime = (A[0], A[1] + dy)
B_prime = (B[0], B[1] + dy)
C_prime = (C[0], C[1] + dy)
D_prime = (D[0], D[1] + dy)
E_prime = (E[0], E[1] + dy)
F_prime = (F[0], F[1] + dy)

# 3. Inicialização da Figura
fig, ax = plt.subplots(figsize=(7, 6))

# 4. Desenhando as arestas visíveis (Sólidas)
# Face superior (Todas visíveis)
top_face = [A, B, C, D, E, F, A]
x_top, y_top = zip(*top_face)
ax.plot(x_top, y_top, 'k-', lw=1.5)

# Arestas verticais frontais e laterais
ax.plot([A[0], A_prime[0]], [A[1], A_prime[1]], 'k-', lw=1.5)
ax.plot([F[0], F_prime[0]], [F[1], F_prime[1]], 'k-', lw=1.5)
ax.plot([E[0], E_prime[0]], [E[1], E_prime[1]], 'k-', lw=1.5)
ax.plot([D[0], D_prime[0]], [D[1], D_prime[1]], 'k-', lw=1.5)

# Arestas da face inferior frontais
bottom_front = [A_prime, F_prime, E_prime, D_prime]
x_bf, y_bf = zip(*bottom_front)
ax.plot(x_bf, y_bf, 'k-', lw=1.5)

# 5. Desenhando as arestas ocultas (Tracejadas)
# Arestas verticais traseiras
ax.plot([B[0], B_prime[0]], [B[1], B_prime[1]], 'k--', lw=1.5)
ax.plot([C[0], C_prime[0]], [C[1], C_prime[1]], 'k--', lw=1.5)

# Arestas da face inferior traseiras
ax.plot([A_prime[0], B_prime[0]], [A_prime[1], B_prime[1]], 'k--', lw=1.5)
ax.plot([B_prime[0], C_prime[0]], [B_prime[1], C_prime[1]], 'k--', lw=1.5)
ax.plot([C_prime[0], D_prime[0]], [C_prime[1], D_prime[1]], 'k--', lw=1.5)

# 6. Adicionando os Rótulos
fontsize = 16
offset = 0.2

# Rótulos Superiores
ax.text(A[0] - offset, A[1], 'A', fontsize=fontsize, ha='right', va='center')
ax.text(B[0], B[1] + offset, 'B', fontsize=fontsize, ha='center', va='bottom')
ax.text(C[0], C[1] + offset, 'C', fontsize=fontsize, ha='center', va='bottom')
ax.text(D[0] + offset, D[1], 'D', fontsize=fontsize, ha='left', va='center')
# E e F recuados para não sobrepor as linhas verticais
ax.text(E[0] - offset, E[1] - offset, 'E', fontsize=fontsize, ha='right', va='top')
ax.text(F[0] + offset, F[1] - offset, 'F', fontsize=fontsize, ha='left', va='top')

# Rótulos Inferiores
ax.text(A_prime[0] - offset, A_prime[1] - offset, "A'", fontsize=fontsize, ha='right', va='top')
ax.text(B_prime[0] + offset, B_prime[1] + offset/2, "B'", fontsize=fontsize, ha='left', va='bottom')
ax.text(C_prime[0] - offset, C_prime[1] + offset/2, "C'", fontsize=fontsize, ha='right', va='bottom')
ax.text(D_prime[0] + offset, D_prime[1] - offset, "D'", fontsize=fontsize, ha='left', va='top')
ax.text(E_prime[0], E_prime[1] - offset, "E'", fontsize=fontsize, ha='center', va='top')
ax.text(F_prime[0], F_prime[1] - offset, "F'", fontsize=fontsize, ha='center', va='top')

# 7. Finalização e Exportação
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('dominio_hexagonal.svg', format='svg', transparent=True)
print("Arquivo 'dominio_hexagonal.svg' gerado com sucesso!")