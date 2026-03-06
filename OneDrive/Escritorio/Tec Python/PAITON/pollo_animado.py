import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ================================================================
#  PASO 1 – MATRICES DE TRANSFORMACIÓN HOMOGÉNEAS (3 × 3)
#  Toda transformación 2D = multiplicación matricial sobre
#  coordenadas homogéneas [x, y, 1]ᵀ
# ================================================================

def T(tx, ty):
    """Traslación: [x,y] → [x+tx, y+ty]"""
    return np.array([[1, 0, tx],
                     [0, 1, ty],
                     [0, 0,  1]], dtype=float)

def R(a):
    """Rotación antihoraria por ángulo a (radianes)"""
    c, s = np.cos(a), np.sin(a)
    return np.array([[ c, -s, 0],
                     [ s,  c, 0],
                     [ 0,  0, 1]], dtype=float)

def S(sx, sy=None):
    """Escalado / reflejo: S(-1,1) espeja en eje Y"""
    if sy is None: sy = sx
    return np.array([[sx,  0, 0],
                     [ 0, sy, 0],
                     [ 0,  0, 1]], dtype=float)

def rot_piv(px, py, a):
    """Rotación alrededor del punto (px, py).
       Composición matricial:  T(p) · R(a) · T(-p)
    """
    return T(px, py) @ R(a) @ T(-px, -py)

def aplica(M, pts):
    """Aplica la transformación M (3×3) a pts (2×N).

    1. Convierte a coordenadas homogéneas: apila fila de 1s → (3×N)
    2. Multiplica matrices: M @ pts_h
    3. Proyecta de vuelta a cartesianas: descarta fila 3
    """
    N_pts = pts.shape[1]
    pts_h = np.vstack([pts, np.ones(N_pts)])   # (3, N)
    res   = M @ pts_h                           # (3, N) ← multiplicación matricial
    return res[:2]                              # (2, N)

# ================================================================
#  PASO 2 – GEOMETRÍA DEL POLLO (idéntica al original, 2×N)
# ================================================================
t  = np.linspace(0, 2 * np.pi, 80)
th = np.linspace(-np.pi / 2, np.pi / 2, 50)

POLLO = {
    'cuerpo'  : np.array([2.0 * np.cos(t),          1.3 * np.sin(t) + 1.5   ]),
    'cabeza'  : np.array([0.85 * np.cos(t) + 2.3,   0.85 * np.sin(t) + 3.0  ]),
    'pico'    : np.array([[3.0, 3.7, 3.0, 3.0],      [3.2, 3.0, 2.8, 3.2]   ]),
    'cresta'  : np.array([[1.8, 2.0, 2.1, 2.3, 2.4, 2.6, 2.8],
                           [3.7, 4.2, 3.9, 4.3, 4.0, 4.2, 3.7]]),
    'barbilla': np.array([0.18 * np.cos(t) + 2.9,   0.22 * np.sin(t) + 2.5  ]),
    'ojo'     : np.array([0.12 * np.cos(t) + 2.45,  0.12 * np.sin(t) + 3.2  ]),
    'ala'     : np.array([1.1 * np.cos(th) + 0.2,   0.55 * np.sin(th) + 1.5 ]),
    'cola1'   : np.array([[-1.9, -2.8, -3.2, -2.4], [1.8, 2.8, 3.8, 2.6]   ]),
    'cola2'   : np.array([[-1.9, -3.0, -3.5, -2.6], [1.5, 2.3, 3.3, 2.2]   ]),
    'cola3'   : np.array([[-1.9, -2.6, -3.0, -2.2], [2.1, 3.2, 4.1, 3.0]   ]),
    'pata_izq': np.array([[-0.4, -0.5, -0.9, -0.5, -0.1, -0.5],
                           [ 0.2, -0.6, -0.9, -0.6, -0.9, -0.6]]),
    'pata_der': np.array([[ 0.6,  0.5,  0.1,  0.5,  0.9,  0.5],
                           [ 0.2, -0.6, -0.9, -0.6, -0.9, -0.6]]),
}
PUPILA = np.array([[2.45], [3.2]])

# Puntos de pivote (en espacio local del pollo)
PIV_PATA_IZQ = (-0.4,  0.2)   # cadera izquierda
PIV_PATA_DER = ( 0.6,  0.2)   # cadera derecha
PIV_ALA      = ( 0.5,  2.0)   # hombro del ala

# ================================================================
#  PASO 3 – MATRICES DE TRANSFORMACIÓN POR FRAME
# ================================================================
N_FRAMES = 120      # frames por ciclo completo de ida y vuelta

def matrices_frame(i):
    """Calcula las 4 matrices de transformación para el frame i.

    Transformaciones aplicadas (todas por multiplicación matricial):
      Mg  = T(tx, ty) [@ S(-1,1)]  ← traslación global + posible reflejo
      Mpi = Mg @ rot_piv(cadera_izq, ang)  ← rotación de pata izquierda
      Mpd = Mg @ rot_piv(cadera_der, -ang) ← rotación de pata derecha
      Mal = Mg @ rot_piv(hombro, ang_ala)  ← bateo del ala
    """
    phi = 2 * np.pi * i / N_FRAMES        # fase cíclica [0, 2π)

    # 1. Traslación: seno suave entre -9 y +9
    tx = 9.0 * np.sin(phi)
    # 2. Rebote vertical: 2 cimas por ciclo completo
    ty = 0.18 * abs(np.sin(2 * phi))

    # 3. Dirección de marcha → S(-1,1) cuando va hacia la izquierda
    va_derecha = np.cos(phi) >= 0
    if va_derecha:
        Mg = T(tx, ty)              # solo traslación
    else:
        Mg = T(tx, ty) @ S(-1, 1)  # traslación ∘ reflejo en Y

    # 4. Patas: oscilan 4 veces por ciclo, con fase opuesta
    ang_paso = 0.45 * np.sin(4 * phi)
    Mpi = Mg @ rot_piv(*PIV_PATA_IZQ,  ang_paso)
    Mpd = Mg @ rot_piv(*PIV_PATA_DER, -ang_paso)

    # 5. Ala: bate suavemente desfasado
    ang_ala = 0.28 * np.sin(2 * phi + np.pi / 4)
    Mal = Mg @ rot_piv(*PIV_ALA, ang_ala)

    return Mg, Mpi, Mpd, Mal

# ================================================================
#  PASO 4 – ANIMACIÓN
# ================================================================
fig, ax = plt.subplots(figsize=(14, 6.5))

def update(i):
    ax.cla()

    # Escena
    ax.set_xlim(-14, 14)
    ax.set_ylim(-1.8, 7.0)
    ax.set_aspect('equal')
    ax.set_facecolor('#ddeeff')
    ax.axhline(-0.88, color='#7a5c2e', lw=2.5, alpha=0.8, zorder=1)
    ax.fill_between([-14, 14], -1.8, -0.88, color='#c4a45e', alpha=0.45, zorder=0)
    ax.grid(True, alpha=0.15, axis='y')

    # Obtener matrices del frame actual
    Mg, Mpi, Mpd, Mal = matrices_frame(i)
    g = lambda k: aplica(Mg, POLLO[k])   # shorthand: aplica Mg a la parte k

    # ── Orden de capas: cola → cuerpo → ala → detalles → patas ──

    # Plumas de cola (fondo)
    for nombre in ('cola1', 'cola2', 'cola3'):
        p = g(nombre)
        ax.fill(p[0], p[1], color='#E67E22', ec='#A04000', lw=2, zorder=2)

    # Cuerpo y cabeza
    cu = g('cuerpo')
    ax.fill(cu[0], cu[1], color='#FFD966', ec='#B8860B', lw=2, zorder=3)
    ca = g('cabeza')
    ax.fill(ca[0], ca[1], color='#FFD966', ec='#B8860B', lw=2, zorder=3)

    # Ala (con rotación de hombro independiente)
    al = aplica(Mal, POLLO['ala'])
    ax.fill(al[0], al[1], color='#F0C040', ec='#B8860B', lw=1.5, zorder=4)

    # Cresta, barbilla, pico
    cr = g('cresta')
    ax.fill(cr[0], cr[1], color='#E74C3C', ec='#C0392B', lw=2, zorder=5)
    ba = g('barbilla')
    ax.fill(ba[0], ba[1], color='#E74C3C', ec='#C0392B', lw=1.5, zorder=5)
    pk = g('pico')
    ax.fill(pk[0], pk[1], color='#F39C12', ec='#D68910', lw=2, zorder=5)

    # Ojo + pupila
    oj = g('ojo')
    ax.fill(oj[0], oj[1], color='white', ec='black', lw=1.5, zorder=6)
    pu = aplica(Mg, PUPILA)
    ax.plot(pu[0], pu[1], 'ko', ms=4, zorder=7)

    # Patas (al frente para que sean visibles)
    pi = aplica(Mpi, POLLO['pata_izq'])
    ax.plot(pi[0], pi[1], color='#D4840A', lw=3, solid_capstyle='round', zorder=8)
    pd = aplica(Mpd, POLLO['pata_der'])
    ax.plot(pd[0], pd[1], color='#D4840A', lw=3, solid_capstyle='round', zorder=8)

    # ── Panel: muestra la matriz global activa ─────────────────
    m = Mg
    mat_str = (
        "M_global (3×3) =\n"
        f"[ {m[0,0]:+.3f}  {m[0,1]:+.3f}  {m[0,2]:+.3f} ]\n"
        f"[ {m[1,0]:+.3f}  {m[1,1]:+.3f}  {m[1,2]:+.3f} ]\n"
        f"[ {m[2,0]:+.3f}  {m[2,1]:+.3f}  {m[2,2]:+.3f} ]"
    )
    ax.text(-13.5, 6.7, mat_str,
            fontfamily='monospace', fontsize=8.5, va='top',
            bbox=dict(boxstyle='round,pad=0.5', fc='lightyellow',
                      ec='#888', alpha=0.93), zorder=9)

    # ── Título informativo ─────────────────────────────────────
    tx_val   = 9.0 * np.sin(2 * np.pi * i / N_FRAMES)
    ang_grad = np.degrees(0.45 * np.sin(4 * 2 * np.pi * i / N_FRAMES))
    dir_txt  = '→ derecha' if np.cos(2 * np.pi * i / N_FRAMES) >= 0 else '← izquierda'
    ax.set_title(
        f'Pollo en movimiento — Transformaciones matriciales (coordenadas homogeneas)\n'
        f'tx = {tx_val:+.2f}   |   theta_pata = {ang_grad:+.1f} deg'
        f'   |   Direccion: {dir_txt}   |   Frame {i+1}/{N_FRAMES}',
        fontsize=11
    )
    return []

ani = animation.FuncAnimation(
    fig, update,
    frames=N_FRAMES,
    interval=40,       # ~25 fps
    blit=False,
    repeat=True
)

plt.tight_layout()
plt.show()

# ── Guardar como GIF (requiere Pillow: pip install pillow) ──────
# writer = animation.PillowWriter(fps=25)
# ani.save('pollo_caminando.gif', writer=writer, dpi=100)
# print("GIF guardado como pollo_caminando.gif")
