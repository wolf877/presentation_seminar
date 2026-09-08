import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io

# Parâmetros
R = 1.0
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = R * np.outer(np.cos(u), np.sin(v))
y = R * np.outer(np.sin(u), np.sin(v))
z = R * np.outer(np.ones(np.size(u)), np.cos(v))

# Clones desalinhados
clone_centers = [
    (0.9, -0.8, 1.1),    # Superior, frente, direita
    (-1.3, 0.2, -0.4),   # Esquerda, quase no equador
    (0.1, 1.4, 0.5),     # Fundo, levemente acima
    (0.6, 0.9, -1.2)     # Fundo, baixo, direita
]

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_axis_off()
fig.patch.set_alpha(0.0)
ax.patch.set_alpha(0.0)

# Plotando as superfícies
ax.plot_surface(x, y, z, color='black', rstride=2, cstride=2, linewidth=0, antialiased=True, edgecolors=None)
for cx, cy, cz in clone_centers:
    ax.plot_surface(x + cx, y + cy, z + cz, color='#003366', rstride=2, cstride=2, linewidth=0, antialiased=True, edgecolors=None, shade=True, alpha=.85)
    
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.6, 1.6)
ax.set_zlim(-1.6, 1.6)
ax.set_box_aspect([1, 1, 1])

# Renderizando os frames manualmente na memória para forçar a limpeza do fundo
frames = []
for angle in range(0, 360, 2): # Pulo de 4 graus garante fluidez
    ax.view_init(elev=20, azim=angle)
    buf = io.BytesIO()
    fig.savefig(buf, format='png', transparent=True)
    buf.seek(0)
    frames.append(Image.open(buf).convert("RGBA"))

# Salvar GIF resolvendo o problema de sobreposição (disposal=2 limpa o quadro anterior)
frames[0].save(
    "figs/lss_matching_circles.gif", 
    save_all=True, 
    append_images=frames[1:], 
    optimize=False, 
    duration=40, 
    loop=0,
    disposal=2 
)
print("GIF gerado com sucesso, sem rastros!")