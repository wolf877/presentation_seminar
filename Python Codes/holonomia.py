import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configuração da figura com dois painéis (Base e Recobrimento)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4), gridspec_kw={'width_ratios': [1, 2]})

# ==========================================
# PAINEL 1: Variedade Base M
# ==========================================
ax1.set_xlim(-0.2, 1.2)
ax1.set_ylim(-0.2, 1.2)
ax1.axis('off')

# Domínio Fundamental (bordas tracejadas indicando colagem)
rect1 = patches.Rectangle((0, 0), 1, 1, linewidth=1.5, edgecolor='black', facecolor='none', linestyle='--')
ax1.add_patch(rect1)

# Ponto x original
ax1.plot(0.5, 0.5, 'ko', markersize=6)
ax1.text(0.35, 0.55, r'$x$', fontsize=16)

# Laço gamma (sai pela direita, entra pela esquerda)
ax1.annotate("", xy=(1, 0.7), xytext=(0.5, 0.5), 
             arrowprops=dict(arrowstyle="-", color="blue", connectionstyle="arc3,rad=-0.3", lw=1.5))
ax1.annotate("", xy=(0.5, 0.5), xytext=(0, 0.7), 
             arrowprops=dict(arrowstyle="->", color="blue", connectionstyle="arc3,rad=-0.3", lw=1.5))
ax1.text(0.75, 0.8, r'$\gamma$', color='blue', fontsize=16)
ax1.set_title(r'Variedade Base $\mathcal{M}$', fontsize=16, y=-0.1)


# ==========================================
# PAINEL 2: Espaço de Recobrimento M_tilde
# ==========================================
ax2.set_xlim(-0.2, 3.2)
ax2.set_ylim(-0.2, 1.2)
ax2.axis('off')

# Células adjacentes (reticulado pontilhado sutil)
for i in range(3):
    rect = patches.Rectangle((i, 0), 1, 1, linewidth=1, edgecolor='gray', facecolor='none', linestyle=':')
    ax2.add_patch(rect)

# Pontos homólogos
ax2.plot(0.5, 0.5, 'ko', markersize=6)
ax2.text(0.35, 0.55, r'$\tilde{x}$', fontsize=16)

ax2.plot(1.5, 0.5, 'ko', markersize=6)
ax2.text(1.35, 0.55, r"$\tilde{x}'$", fontsize=16)

ax2.plot(2.5, 0.5, 'ko', markersize=6)
ax2.text(2.35, 0.55, r"$\tilde{x}''$", fontsize=16)

# Caminho desdobrado (levantamento do laço)
ax2.annotate("", xy=(1.5, 0.5), xytext=(0.5, 0.5), 
             arrowprops=dict(arrowstyle="->", color="blue", connectionstyle="arc3,rad=-0.5", lw=1.5))
ax2.text(1.0, 0.85, r'$\tilde{\gamma}$', color='blue', fontsize=16)

# Ação do Grupo de Holonomia (Vetor vermelho conectando os pontos)
ax2.annotate("", xy=(1.5, 0.3), xytext=(0.5, 0.3), 
             arrowprops=dict(arrowstyle="->", color="red", lw=2))
ax2.text(0.95, 0.15, r'$\Gamma$', color='red', fontsize=16)

ax2.set_title(r'Espaço de Recobrimento $\tilde{\mathcal{M}}$', fontsize=16, y=-0.1)

# ==========================================
# Exportação
# ==========================================
plt.tight_layout()
plt.savefig('ação_holonomia.svg', format='svg', transparent=True)
print("Arquivo 'ação_holonomia.svg' gerado com sucesso!")