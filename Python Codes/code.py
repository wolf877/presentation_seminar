import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def gerar_ruido_cmb(nx, ny, alpha=1.5): # <- AQUI: Reduzi para 0.8 para ficar bem granulado
    ruido = np.random.normal(0, 1, (ny, nx))
    fft_ruido = np.fft.fft2(ruido)
    fft_ruido = np.fft.fftshift(fft_ruido)
    
    kx = np.fft.fftfreq(nx)
    ky = np.fft.fftfreq(ny)
    kx, ky = np.fft.fftshift(kx), np.fft.fftshift(ky)
    kx_grid, ky_grid = np.meshgrid(kx, ky)
    k = np.sqrt(kx_grid**2 + ky_grid**2)
    
    centro_x, centro_y = nx // 2, ny // 2
    k[centro_y, centro_x] = 1.0  
    
    filtro = k ** (-alpha)
    filtro[centro_y, centro_x] = 0  
    
    fft_filtrada = fft_ruido * filtro
    mapa = np.fft.ifft2(np.fft.ifftshift(fft_filtrada)).real
    return mapa

nx, ny = 960, 540 
mapa = gerar_ruido_cmb(nx, ny, alpha=2.) # Mais textura fina
mapa_norm = (mapa - mapa.min()) / (mapa.max() - mapa.min())

# --- COMO CRIAR O SEU PRÓPRIO MAPA DE CORES ---
# Defina a cor dos "vales", o meio (branco/transparente) e os "picos"
cor_fria = '#003366'   # Roxo 
cor_centro = '#FFFFFF' # Branco
cor_quente = '#61172b' # Laranja

cores_customizadas = [cor_fria, cor_centro, cor_quente]
meu_cmap = LinearSegmentedColormap.from_list('meu_cmap', cores_customizadas)

# Aplica as suas cores na imagem
rgba_img = meu_cmap(mapa_norm)

# --- APLICA A TRANSPARÊNCIA ---
dist_from_center = np.abs(mapa_norm - 0.5) * 2 
rgba_img[:, :, 3] = np.clip(dist_from_center ** .3, 0, 1) 

fig, ax = plt.subplots(figsize=(16, 9), dpi=600)
ax.imshow(rgba_img, interpolation='bicubic')
ax.axis('off')

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
plt.savefig('cmb_custom.svg', format='svg', transparent=True, bbox_inches='tight', pad_inches=0)