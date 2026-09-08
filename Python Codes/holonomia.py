import numpy as np
import matplotlib.pyplot as plt

# Configuração global para usar LaTeX nas fontes (opcional, mas fica mais bonito)
plt.rcParams.update({
    "text.usetex": True, # Mude para True se tiver um compilador LaTeX instalado no sistema
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 14
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Coordenadas do loop
x_start = 0.2
y_start = 0.5
x_end_cover = x_start + 1.0 # Translação por uma célula
y_end_cover = y_start       # Retorna à mesma altura para um E1 (translação pura)

# Criando a curva suave (lift no espaço de recobrimento)
t = np.linspace(0, 1, 150)
x_cover = x_start + t
y_cover = y_start + 0.3 * np.sin(np.pi * t)

# ==========================================
# PAINEL 1: A Variedade M (Visão do Observador)
# ==========================================
#ax1.set_title(r"Variedade Compacta $\mathcal{M}$", pad=20, fontweight='bold')

# Desenhando o domínio fundamental
ax1.fill_between([0, 1], 0, 1, color='black', alpha=0.1)
ax1.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color='black', lw=1.5)

# Dividindo a curva contínua nas partes que "reaparecem" na variedade
mask1 = x_cover <= 1.0
mask2 = x_cover > 1.0

# Trecho 1 (do ponto inicial até a borda direita)
ax1.plot(x_cover[mask1], y_cover[mask1], color='black', lw=2.5)
# Trecho 2 (reaparece na borda esquerda e fecha no ponto inicial)
ax1.plot(x_cover[mask2] - 1.0, y_cover[mask2], color='black', lw=2.5)

# Ponto x
ax1.plot(x_start, y_start, 'o', color='black',markersize=9, zorder=5)
ax1.text(x_start, y_start - 0.09, r'$\vec x$', color='black', fontsize=28)

# Indicando que é um loop fechado (\gamma)
ax1.text(0.6, 0.85, r'$\gamma$', color='black', fontsize=30)
ax1.text(.05, .90, r'$\mathcal{M}$', color='black', fontsize=30)
# Setas indicando a identificação (Topologia de toro/cilindro)
ax1.annotate('', xy=(1.05, 0.5), xytext=(0.95, 0.5), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax1.annotate('', xy=(0.05, 0.5), xytext=(-0.05, 0.5), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

ax1.set_xlim(-0.1, 1.1)
ax1.set_ylim(-0.1, 1.1)
ax1.set_aspect('equal')
ax1.axis('off')

# ==========================================
# PAINEL 2: Espaço de Recobrimento Universal (\tilde{M})
# ==========================================
#ax2.set_title("Espaço de Recobrimento $\\tilde{M}$", pad=20, fontweight='bold')

# Desenhando a malha de recobrimento (3 células)
for i in range(-1, 3):
    ax2.axvline(i, color='gray', linestyle='--', alpha=0.5)
    ax2.axhline(0, color='gray', linestyle='--', alpha=0.5)
    ax2.axhline(1, color='gray', linestyle='--', alpha=0.5)

# Colorindo o domínio fundamental original para referência
ax2.fill_between([0, 1], 0, 1, color='black', alpha=0.1)

# Traçando o Lift contínuo (A verdadeira trajetória da luz)
ax2.plot(x_cover, y_cover, color='black', lw=2.5)

# Ponto inicial e final deslocado
ax2.plot(x_start, y_start, 'ko', markersize=9, zorder=5)
ax2.plot(x_end_cover, y_end_cover, 'ko', markersize=9, zorder=5)

ax2.text(x_start, y_start - 0.19, r'$\vec{\tilde{x}}$', color='black', fontsize=28)
ax2.text(x_end_cover, y_end_cover - 0.19, r'$\vec{\tilde{x}}^\prime = g\vec{\tilde{x}}$', color='black', fontsize=28)
ax2.text(0.5, 0.87, r'$\tilde{\gamma}$', color='black', fontsize=30)
ax2.text(2.2, 1.3, r'$\mathcal{C}$', fontsize=30)

# # Vetor de deslocamento (Holonomia)
# ax2.annotate('', xy=(x_end_cover, y_start - 0.15), xytext=(x_start, y_start - 0.15),
#              arrowprops=dict(arrowstyle='->', color='black', lw=2, ls=':'))
# ax2.text(0.7, y_start - 0.25, r'Deslocamento pela holonomia', ha='center', fontsize=12, fontweight='bold')

ax2.set_xlim(-0.5, 2.5)
ax2.set_ylim(-0.5, 1.5)
ax2.set_aspect('equal')
ax2.axis('off')

# ==========================================
# SALVANDO OS ARQUIVOS SEM FUNDO
# ==========================================
plt.tight_layout()

# Exporta para PDF mantendo texto em vetor
plt.savefig('holonomia_comparacao.pdf', format='pdf', transparent=True, bbox_inches='tight')
# Exporta para SVG perfeito para web/Quarto
plt.savefig('figs/holonomy.svg', format='svg', transparent=True, bbox_inches='tight')

#plt.show()