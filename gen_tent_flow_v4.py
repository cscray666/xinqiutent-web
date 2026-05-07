import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Arc, Wedge, Ellipse, FancyArrowPatch
from matplotlib.path import Path
import matplotlib.patheffects as pe
import numpy as np

# ══════════════════════════════════════════════════════════════════════════
# CANVAS  — wide landscape, no wasted space
# ══════════════════════════════════════════════════════════════════════════
FIG_W, FIG_H = 32, 15
fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
ax.set_xlim(0, FIG_W); ax.set_ylim(0, FIG_H)
ax.axis('off')
BG = '#0D1F2D'
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)

# ══════════════════════════════════════════════════════════════════════════
# STEPS  (corrected order)
# ══════════════════════════════════════════════════════════════════════════
steps = [
    {
        "num": "01",
        "title": "Fabric Weaving\n& Production",
        "desc": "Polyester / Nylon\nBase Cloth Weaving",
        "note": "Supplier Mill",
        "color": "#E8643A",
    },
    {
        "num": "02",
        "title": "Surface Coating\nTreatment",
        "desc": "PU · Flame Retardant\nUV · Silver Coating",
        "note": "Done at Mill",
        "color": "#F0A800",
    },
    {
        "num": "03",
        "title": "Fabric Cutting\n& Patterning",
        "desc": "CNC Die-Cut\nTemplate Matching",
        "note": "In-Factory",
        "color": "#27AE60",
    },
    {
        "num": "04",
        "title": "Sewing &\nStitching",
        "desc": "Industrial Sewing\nDouble-Seam & Bar-Tack",
        "note": "In-Factory",
        "color": "#1E8BC3",
    },
    {
        "num": "05",
        "title": "Pole & Frame\nAssembly",
        "desc": "Fiberglass / Alloy\nShock-Cord Rigging",
        "note": "In-Factory",
        "color": "#9B59B6",
    },
    {
        "num": "06",
        "title": "Component\nIntegration",
        "desc": "Tent Body · Flysheet\nStakes & Guy Lines",
        "note": "In-Factory",
        "color": "#E8643A",
    },
    {
        "num": "07",
        "title": "Quality Control\n& Testing",
        "desc": "Water · Wind\nLoad Resistance Test",
        "note": "QC Lab",
        "color": "#F0A800",
    },
    {
        "num": "08",
        "title": "Packaging\n& Labeling",
        "desc": "Folding · Bagging\nBarcode & Care Label",
        "note": "In-Factory",
        "color": "#27AE60",
    },
    {
        "num": "09",
        "title": "Warehousing\n& Shipping",
        "desc": "Inventory Control\nExport & Delivery",
        "note": "Warehouse",
        "color": "#1E8BC3",
    },
]
N = len(steps)

# ══════════════════════════════════════════════════════════════════════════
# LAYOUT
# ══════════════════════════════════════════════════════════════════════════
PAD_L, PAD_R = 0.55, 0.55
TOTAL_W   = FIG_W - PAD_L - PAD_R   # 30.9
STEP_W    = TOTAL_W / N              # ~3.43
CARD_W    = STEP_W * 0.86
CARD_H    = 9.6
BELT_Y    = 3.2
BELT_H    = 0.65
CARD_BY   = BELT_Y + BELT_H         # card bottom
CARD_TY   = CARD_BY + CARD_H        # card top
ICON_R    = 0.92                     # icon circle radius
ICON_CY   = CARD_TY - ICON_R - 0.28

# ══════════════════════════════════════════════════════════════════════════
# BACKGROUND GRID (subtle)
# ══════════════════════════════════════════════════════════════════════════
for gx in np.arange(0, FIG_W, 2.0):
    ax.plot([gx, gx], [0, FIG_H], color='#1A3040', lw=0.4, zorder=0)
for gy in np.arange(0, FIG_H, 2.0):
    ax.plot([0, FIG_W], [gy, gy], color='#1A3040', lw=0.4, zorder=0)

# ══════════════════════════════════════════════════════════════════════════
# VECTOR ICON DRAWING
# ══════════════════════════════════════════════════════════════════════════
def draw_icon(ax, idx, cx, cy, r, col):
    s = r * 0.62   # icon scale

    if idx == 0:   # ── Loom / weave grid ──────────────────────────────
        # warp threads (vertical)
        for xi in np.linspace(cx - s*0.7, cx + s*0.7, 6):
            ax.plot([xi, xi], [cy - s*0.75, cy + s*0.75],
                    color='white', lw=1.8, alpha=0.9, zorder=12)
        # weft threads (horizontal)
        for yi in np.linspace(cy - s*0.6, cy + s*0.6, 5):
            ax.plot([cx - s*0.72, cx + s*0.72], [yi, yi],
                    color='#FFD580', lw=2.2, alpha=0.95, zorder=13)
        # shuttle
        shuttle_pts = np.array([[cx - s*0.72, cy + s*0.72],
                                  [cx + s*0.72, cy + s*0.72]])
        ax.add_patch(FancyBboxPatch((cx - s*0.72, cy + s*0.55), s*1.44, s*0.28,
                                    boxstyle='round,pad=0.04',
                                    color=col, ec='white', lw=1.2, zorder=14))

    elif idx == 1:  # ── Coating / paint roller ──────────────────────
        # roller handle
        ax.plot([cx - s*0.55, cx + s*0.1], [cy + s*0.7, cy - s*0.0],
                color='white', lw=3.0, solid_capstyle='round', zorder=12)
        # roller head
        ax.add_patch(FancyBboxPatch((cx - s*0.15, cy - s*0.55), s*0.75, s*0.40,
                                    boxstyle='round,pad=0.06',
                                    color='white', zorder=12))
        # paint drip
        for dp, dy_off in [(cx + s*0.1, -0.2), (cx + s*0.35, -0.35), (cx + s*0.55, -0.2)]:
            ax.add_patch(Ellipse((dp, cy - s*0.9 + dy_off), s*0.14, s*0.28,
                                  color=col, alpha=0.9, zorder=13))
        # rainbow stripe on roller
        for ci, cc in enumerate(['#E8643A','#F0A800','#27AE60','#1E8BC3']):
            ax.add_patch(Rectangle((cx - s*0.13 + ci*s*0.16, cy - s*0.53),
                                    s*0.14, s*0.36, color=cc, zorder=13))

    elif idx == 2:  # ── Cutting / scissors + fabric ─────────────────
        # fabric piece (parallelogram)
        fx = [cx-s*0.7, cx+s*0.1, cx+s*0.7, cx-s*0.1, cx-s*0.7]
        fy = [cy-s*0.3, cy-s*0.3, cy+s*0.3, cy+s*0.3, cy-s*0.3]
        ax.fill(fx, fy, color='white', alpha=0.18, zorder=11)
        ax.plot(fx, fy, color='white', lw=1.2, alpha=0.5, zorder=12)
        # dashed cut line
        ax.plot([cx-s*0.7, cx+s*0.7], [cy, cy],
                color='#FFD580', lw=1.8, ls='--', dashes=(4,3), zorder=12)
        # scissors body
        for sign in [1, -1]:
            ax.plot([cx + s*0.0, cx + s*0.72],
                    [cy, cy + sign*s*0.55],
                    color='white', lw=2.8, solid_capstyle='round', zorder=13)
            ax.add_patch(Circle((cx - s*0.18, cy + sign*s*0.22), s*0.22,
                                color='none', ec='white', lw=2.2, zorder=13))
        ax.add_patch(Circle((cx, cy), s*0.12, color=col, zorder=14))

    elif idx == 3:  # ── Sewing machine ──────────────────────────────
        # machine body
        ax.add_patch(FancyBboxPatch((cx-s*0.72, cy-s*0.55), s*1.1, s*0.75,
                                    boxstyle='round,pad=0.08',
                                    color='white', alpha=0.92, zorder=12))
        # arm
        ax.add_patch(FancyBboxPatch((cx-s*0.55, cy+s*0.2), s*0.9, s*0.32,
                                    boxstyle='round,pad=0.06',
                                    color='white', alpha=0.75, zorder=12))
        # needle
        ax.plot([cx+s*0.28, cx+s*0.28], [cy+s*0.2, cy-s*0.55],
                color=col, lw=2.4, zorder=13)
        ax.add_patch(Ellipse((cx+s*0.28, cy-s*0.55), s*0.1, s*0.16,
                              color='#FFD580', zorder=14))
        # stitch line
        for xi in np.linspace(cx-s*0.6, cx+s*0.5, 8):
            ax.add_patch(Rectangle((xi, cy-s*0.72), s*0.07, s*0.12,
                                    color='#FFD580', zorder=13))
        # flywheel
        ax.add_patch(Circle((cx-s*0.42, cy+s*0.36), s*0.25,
                             color=col, ec='white', lw=1.5, zorder=13))
        ax.add_patch(Circle((cx-s*0.42, cy+s*0.36), s*0.10,
                             color='white', zorder=14))

    elif idx == 4:  # ── Tent pole / aluminum tube ───────────────────
        # main pole diagonal
        ax.plot([cx-s*0.65, cx+s*0.65], [cy-s*0.6, cy+s*0.6],
                color='white', lw=5.5, solid_capstyle='round',
                path_effects=[pe.withStroke(linewidth=7, foreground=col)],
                zorder=12)
        # cross pole
        ax.plot([cx-s*0.5, cx+s*0.5], [cy+s*0.4, cy-s*0.5],
                color='#B0C8D8', lw=4.0, solid_capstyle='round', zorder=12)
        # shock cord coil
        coil_x = np.linspace(cx-s*0.3, cx+s*0.3, 30)
        coil_y = cy + s*0.05 + s*0.12*np.sin(np.linspace(0, 6*np.pi, 30))
        ax.plot(coil_x, coil_y, color='#FFD580', lw=1.8, zorder=13)
        # ferrule caps
        for ex, ey in [(cx-s*0.65, cy-s*0.6),(cx+s*0.65, cy+s*0.6)]:
            ax.add_patch(Circle((ex, ey), s*0.12, color=col,
                                ec='white', lw=1.2, zorder=14))

    elif idx == 5:  # ── Full tent assembly illustration ──────────────
        # ground shadow ellipse
        ax.add_patch(Ellipse((cx, cy-s*0.72), s*1.6, s*0.22,
                              color='#000', alpha=0.25, zorder=11))
        # flysheet (outer tent)
        fly_x = [cx-s*0.9, cx, cx+s*0.9, cx+s*0.6, cx-s*0.6, cx-s*0.9]
        fly_y = [cy-s*0.6, cy+s*0.82, cy-s*0.6, cy-s*0.6, cy-s*0.6, cy-s*0.6]
        ax.fill(fly_x, fly_y, color='#4A7FA5', alpha=0.7, zorder=12)
        ax.plot([cx-s*0.9, cx, cx+s*0.9], [cy-s*0.6, cy+s*0.82, cy-s*0.6],
                color='white', lw=2.2, zorder=13)
        # inner tent
        in_x = [cx-s*0.55, cx, cx+s*0.55]
        in_y = [cy-s*0.55, cy+s*0.45, cy-s*0.55]
        ax.fill(in_x, in_y, color='white', alpha=0.25, zorder=13)
        # door zipper
        ax.add_patch(Wedge((cx, cy-s*0.55), s*0.28, 0, 180,
                            color=col, alpha=0.9, zorder=14))
        # guy lines
        for gx_off, gy_off in [(-s*0.9, -s*0.6),(s*0.9, -s*0.6)]:
            ax.plot([cx + gx_off*0.7, cx + gx_off*1.15],
                    [cy - s*0.2, cy + gy_off*0.85],
                    color='#FFD580', lw=1.5, ls='--', zorder=13)
        # stakes
        for sx_off in [-s*1.1, s*1.1]:
            ax.plot([cx+sx_off, cx+sx_off], [cy-s*0.72, cy-s*0.58],
                    color='#B0C8D8', lw=2.5, solid_capstyle='round', zorder=13)

    elif idx == 6:  # ── QC shield + checkmark ────────────────────────
        # shield outline
        sh_pts = [(cx, cy+s*0.82),(cx+s*0.65, cy+s*0.45),
                  (cx+s*0.65, cy-s*0.15),(cx, cy-s*0.82),
                  (cx-s*0.65, cy-s*0.15),(cx-s*0.65, cy+s*0.45),(cx, cy+s*0.82)]
        ax.fill([p[0] for p in sh_pts],[p[1] for p in sh_pts],
                color='white', alpha=0.18, zorder=12)
        ax.plot([p[0] for p in sh_pts],[p[1] for p in sh_pts],
                color='white', lw=2.2, zorder=13)
        # checkmark
        ax.plot([cx-s*0.32, cx-s*0.02, cx+s*0.42],
                [cy-s*0.02, cy-s*0.38, cy+s*0.45],
                color=col, lw=4.5, solid_capstyle='round',
                solid_joinstyle='round', zorder=14)
        # "QC" text
        ax.text(cx, cy-s*0.6, 'QC', fontsize=8, fontweight='bold',
                color='white', ha='center', va='center', zorder=14)

    elif idx == 7:  # ── Packaging / open box ────────────────────────
        # box body
        ax.add_patch(FancyBboxPatch((cx-s*0.65, cy-s*0.65), s*1.3, s*1.05,
                                    boxstyle='round,pad=0.06',
                                    color='white', alpha=0.88, zorder=12))
        # left flap
        ax.fill([cx-s*0.65, cx-s*0.65, cx, cx],
                [cy+s*0.40, cy+s*0.70, cy+s*0.70, cy+s*0.40],
                color='white', alpha=0.60, zorder=12)
        # right flap
        ax.fill([cx, cx, cx+s*0.65, cx+s*0.65],
                [cy+s*0.40, cy+s*0.70, cy+s*0.70, cy+s*0.40],
                color='white', alpha=0.45, zorder=12)
        ax.plot([cx-s*0.65, cx+s*0.65],[cy+s*0.40, cy+s*0.40],
                color=col, lw=1.8, zorder=13)
        # tape / ribbon
        ax.plot([cx, cx],[cy-s*0.65, cy+s*0.40], color=col, lw=2.5, zorder=13)
        ax.plot([cx-s*0.65, cx+s*0.65],[cy-s*0.10, cy-s*0.10],
                color=col, lw=2.5, zorder=13)
        # label
        ax.add_patch(FancyBboxPatch((cx-s*0.42, cy-s*0.55), s*0.84, s*0.36,
                                    boxstyle='round,pad=0.04',
                                    color=col, alpha=0.8, zorder=14))
        ax.text(cx, cy-s*0.37, 'LABEL', fontsize=6, fontweight='bold',
                color='white', ha='center', va='center', zorder=15)

    elif idx == 8:  # ── Container ship ──────────────────────────────
        # sea waves
        for wy in [cy-s*0.65, cy-s*0.52]:
            wave_x = np.linspace(cx-s*0.9, cx+s*0.9, 40)
            wave_y = wy + s*0.05*np.sin(np.linspace(0, 4*np.pi, 40))
            ax.plot(wave_x, wave_y, color='#4A90D9', lw=2.0, alpha=0.7, zorder=11)
        # hull
        hull_x = [cx-s*0.85, cx-s*0.9, cx+s*0.9, cx+s*0.85, cx-s*0.85]
        hull_y = [cy-s*0.42, cy-s*0.62, cy-s*0.62, cy-s*0.42, cy-s*0.42]
        ax.fill(hull_x, hull_y, color='#2C3E50', zorder=12)
        # main deck
        ax.add_patch(FancyBboxPatch((cx-s*0.82, cy-s*0.42), s*1.64, s*0.36,
                                    boxstyle='round,pad=0.04',
                                    color='#ECF0F1', alpha=0.92, zorder=12))
        # containers (colored boxes)
        cont_colors = ['#E8643A','#1E8BC3','#27AE60','#F0A800','#9B59B6']
        for ci, cc in enumerate(cont_colors):
            ax.add_patch(Rectangle((cx - s*0.72 + ci*s*0.3, cy-s*0.36),
                                    s*0.26, s*0.26, color=cc, zorder=13))
        # bridge / cabin
        ax.add_patch(FancyBboxPatch((cx+s*0.42, cy-s*0.05), s*0.38, s*0.52,
                                    boxstyle='round,pad=0.04',
                                    color='#2C3E50', zorder=13))
        # windows
        for wy2 in [cy+s*0.22, cy+s*0.06]:
            ax.add_patch(Rectangle((cx+s*0.50, wy2), s*0.10, s*0.10,
                                    color='#FFD580', zorder=14))
        # smoke
        smoke_x = np.linspace(cx+s*0.58, cx+s*0.42, 12)
        smoke_y = np.linspace(cy+s*0.5, cy+s*0.85, 12)
        ax.plot(smoke_x + s*0.08*np.sin(np.linspace(0,3,12)),
                smoke_y, color='#B0C8D8', lw=2.5, alpha=0.6, zorder=13)


# ══════════════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════════════
ax.add_patch(FancyBboxPatch((0.3, 12.9), FIG_W-0.6, 1.88,
                             boxstyle='round,pad=0.1',
                             linewidth=0, facecolor='#162533', zorder=1))
# accent bars
for xi, col in [(0.3,'#E8643A'),(0.85,'#F0A800'),(1.28,'#27AE60'),(1.62,'#1E8BC3')]:
    ax.add_patch(Rectangle((xi, 12.9), 0.40, 1.88, color=col, zorder=2))
ax.add_patch(Rectangle((0.3, 12.9), 1.9, 1.88, color='#162533', alpha=0, zorder=1))  # fixer

ax.text(FIG_W/2, 14.08,
        "TENT  MANUFACTURING  PROCESS  FLOW",
        fontsize=32, fontweight='bold', color='#FFFFFF',
        ha='center', va='center', fontfamily='DejaVu Sans', zorder=3)
ax.text(FIG_W/2, 13.34,
        "Corrected Production Sequence  ·  From Raw Fabric to Finished Tent  ·  9 Key Stages",
        fontsize=13.5, color='#7EC8E3',
        ha='center', va='center', fontfamily='DejaVu Sans', zorder=3)

# ══════════════════════════════════════════════════════════════════════════
# CONVEYOR BELT
# ══════════════════════════════════════════════════════════════════════════
ax.add_patch(FancyBboxPatch((PAD_L-0.08, BELT_Y), TOTAL_W+0.16, BELT_H,
                             boxstyle='round,pad=0.08',
                             linewidth=0, facecolor='#1E3A4A', zorder=2))
x_rib = PAD_L + 0.2
while x_rib < PAD_L + TOTAL_W - 0.15:
    ax.add_patch(Rectangle((x_rib, BELT_Y+0.07), 0.26, BELT_H-0.14,
                            color='#2A4A5A', zorder=3))
    x_rib += 0.56
ax.plot([PAD_L, PAD_L+TOTAL_W], [BELT_Y+BELT_H-0.05, BELT_Y+BELT_H-0.05],
        color='#3D6070', lw=2, zorder=4)
for rx in [PAD_L-0.08, PAD_L+TOTAL_W+0.08]:
    ax.add_patch(Circle((rx, BELT_Y+BELT_H/2), BELT_H/2+0.12, color='#1C3A4A', zorder=4))
    ax.add_patch(Circle((rx, BELT_Y+BELT_H/2), BELT_H/2+0.12,
                        color='none', ec='#4A7A90', lw=2.5, zorder=5))

# ══════════════════════════════════════════════════════════════════════════
# CARDS
# ══════════════════════════════════════════════════════════════════════════
PAD_L = 0.55

for i, step in enumerate(steps):
    col = step["color"]
    cx  = PAD_L + i * STEP_W + STEP_W / 2
    card_x = cx - CARD_W / 2

    # shadow
    ax.add_patch(FancyBboxPatch((card_x+0.09, CARD_BY-0.09), CARD_W, CARD_H,
                                boxstyle='round,pad=0.1',
                                linewidth=0, facecolor='#000', alpha=0.40, zorder=4))
    # card body
    ax.add_patch(FancyBboxPatch((card_x, CARD_BY), CARD_W, CARD_H,
                                boxstyle='round,pad=0.1',
                                linewidth=2.2, edgecolor=col,
                                facecolor='#162533', zorder=5))
    # top color bar
    ax.add_patch(FancyBboxPatch((card_x, CARD_BY+CARD_H-0.52), CARD_W, 0.65,
                                boxstyle='round,pad=0.1',
                                linewidth=0, facecolor=col, zorder=6))
    ax.add_patch(Rectangle((card_x, CARD_BY+CARD_H-0.52), CARD_W, 0.32,
                            color=col, zorder=6))

    # step num badge
    ax.add_patch(Circle((card_x+CARD_W-0.36, CARD_BY+CARD_H-0.36), 0.33,
                        color='#0D1F2D', zorder=7))
    ax.text(card_x+CARD_W-0.36, CARD_BY+CARD_H-0.36, step["num"],
            fontsize=10, fontweight='bold', color=col,
            ha='center', va='center', zorder=8)

    # icon circle glow → ring → fill
    ax.add_patch(Circle((cx, ICON_CY), ICON_R+0.22, color=col, alpha=0.16, zorder=6))
    ax.add_patch(Circle((cx, ICON_CY), ICON_R+0.08, color='white', zorder=7))
    ax.add_patch(Circle((cx, ICON_CY), ICON_R, color=col, zorder=8))

    # vector icon
    draw_icon(ax, i, cx, ICON_CY, ICON_R, col)

    # tag: "Supplier Mill" vs "In-Factory"
    tag_col = '#E8643A' if 'Mill' in step["note"] or 'Supplier' in step["note"] else '#27AE60'
    ax.add_patch(FancyBboxPatch((card_x+0.12, CARD_BY+CARD_H-1.22), CARD_W-0.24, 0.30,
                                boxstyle='round,pad=0.04',
                                linewidth=0, facecolor=tag_col, alpha=0.22, zorder=7))
    ax.text(cx, CARD_BY+CARD_H-1.07, step["note"],
            fontsize=7.5, color=tag_col, fontweight='bold',
            ha='center', va='center', zorder=8)

    # title
    title_y = ICON_CY - ICON_R - 0.42
    ax.text(cx, title_y, step["title"],
            fontsize=11.5, fontweight='bold', color='#FFFFFF',
            ha='center', va='top', linespacing=1.55, zorder=9)

    # desc
    ax.text(cx, title_y - 1.35, step["desc"],
            fontsize=9.5, color='#90B8C8',
            ha='center', va='top', linespacing=1.65, zorder=9)

    # bottom accent
    ax.add_patch(Rectangle((card_x+0.18, CARD_BY+0.14), CARD_W-0.36, 0.1,
                            color=col, alpha=0.45, zorder=6))

    # connector arrow
    if i < N - 1:
        ax_s = card_x + CARD_W + 0.06
        ax_e = card_x + STEP_W - 0.06
        a_y  = CARD_BY + CARD_H * 0.52
        ax.annotate('', xy=(ax_e, a_y), xytext=(ax_s, a_y),
                    arrowprops=dict(arrowstyle='->', color=col,
                                   lw=2.8, mutation_scale=18), zorder=10)

    # "Supplier → Factory" divider between step 02 and 03
    if i == 1:
        div_x = card_x + CARD_W + (STEP_W - CARD_W) / 2
        ax.plot([div_x, div_x], [CARD_BY+0.2, CARD_BY+CARD_H-0.2],
                color='#FFD580', lw=1.5, ls='--', alpha=0.6, zorder=10)
        ax.text(div_x, CARD_BY+CARD_H*0.12, 'Delivered\nto Factory',
                fontsize=7.5, color='#FFD580', ha='center', va='bottom',
                zorder=11, style='italic')

# ══════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════
ax.add_patch(FancyBboxPatch((0.3, 0.15), FIG_W-0.6, 1.0,
                             boxstyle='round,pad=0.08',
                             linewidth=0, facecolor='#162533', zorder=2))
ax.text(FIG_W/2, 0.65,
        "Professional Outdoor Gear Manufacturing   ·   "
        "Strict Quality Control at Every Stage   ·   "
        "World-Class Tent Production",
        fontsize=11.5, color='#7EC8E3',
        ha='center', va='center', style='italic', zorder=3)
dot_cols = ["#E8643A","#F0A800","#27AE60","#1E8BC3","#9B59B6"]
for j, dc in enumerate(dot_cols):
    ax.add_patch(Circle((1.2+j*0.52, 0.65), 0.09, color=dc, zorder=4))
    ax.add_patch(Circle((FIG_W-1.2-j*0.52, 0.65), 0.09, color=dc, zorder=4))

# ══════════════════════════════════════════════════════════════════════════
# SAVE
# ══════════════════════════════════════════════════════════════════════════
plt.tight_layout(pad=0)
out = r'C:\Users\Ray\.accio\accounts\1749967330\agents\DID-F456DA-2B0D4C\project\tent_flow_v3.png'
plt.savefig(out, dpi=170, bbox_inches='tight', facecolor=fig.get_facecolor())
print("Saved:", out)
