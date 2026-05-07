import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Arc, Wedge, Ellipse
import numpy as np

fig, ax = plt.subplots(figsize=(28, 13))
ax.set_xlim(0, 28)
ax.set_ylim(0, 13)
ax.axis('off')
fig.patch.set_facecolor('#12232E')
ax.set_facecolor('#12232E')

# ── Colors ───────────────────────────────────────────────────────────────
STEP_COLORS = [
    "#E05C2A",  # 01 orange-red
    "#F0A800",  # 02 amber
    "#27AE60",  # 03 green
    "#1E8BC3",  # 04 blue
    "#8E44AD",  # 05 purple
    "#E05C2A",  # 06
    "#F0A800",  # 07
    "#27AE60",  # 08
    "#1E8BC3",  # 09
]

# ── Step data ─────────────────────────────────────────────────────────────
steps = [
    ("01", "Raw Material\nInspection",    "Fabric · Poles\nZippers · Buckles"),
    ("02", "Fabric Cutting\n& Patterning","CNC Cutting\nTemplate Matching"),
    ("03", "Sewing &\nStitching",         "Industrial Sewing\nSeam Reinforcement"),
    ("04", "Waterproofing\n& Coating",    "PU Coating\nHeat-Seal Seams"),
    ("05", "Pole & Frame\nAssembly",      "Fiberglass Poles\nShock Cord Rigging"),
    ("06", "Component\nIntegration",      "Flysheet · Stakes\nGuy Lines"),
    ("07", "Quality Control\n& Testing",  "Water · Load\nWind Resistance"),
    ("08", "Packaging\n& Labeling",       "Folding · Bagging\nBarcode Labels"),
    ("09", "Warehousing\n& Shipping",     "Inventory Mgmt\nExport & Delivery"),
]
N = len(steps)

# ── Layout ────────────────────────────────────────────────────────────────
ML = 0.6; MR = 0.6
TW = 28 - ML - MR
SW = TW / N          # step width ≈ 3.0
CW = SW * 0.80       # card width
CH = 7.6             # card height
BELT_Y  = 3.4
BELT_H  = 0.6
CARD_BY = BELT_Y + BELT_H          # card bottom y
ICON_R  = 0.75
ICON_CY = CARD_BY + CH - ICON_R - 0.3

# ═══════════════════════════════════════════════════════════════════════════
# HELPER: draw vector icons inside the colored circle
# ═══════════════════════════════════════════════════════════════════════════
def draw_icon(ax, idx, cx, cy, r, col):
    """Draw a simple vector icon for each step."""
    w = r * 0.55   # icon scale
    if idx == 0:   # magnifying glass
        lens = Circle((cx - w*0.1, cy + w*0.1), w*0.55, color='none', ec='white', lw=2.2, zorder=12)
        ax.add_patch(lens)
        ax.plot([cx + w*0.28, cx + w*0.7], [cy - w*0.28, cy - w*0.7],
                color='white', lw=2.5, solid_capstyle='round', zorder=12)

    elif idx == 1:  # scissors
        # blade 1
        ax.plot([cx - w*0.6, cx + w*0.15], [cy + w*0.5, cy],
                color='white', lw=2.2, solid_capstyle='round', zorder=12)
        ax.plot([cx - w*0.6, cx + w*0.15], [cy - w*0.5, cy],
                color='white', lw=2.2, solid_capstyle='round', zorder=12)
        # pivot
        circ = Circle((cx + w*0.15, cy), w*0.18, color='white', zorder=12)
        ax.add_patch(circ)
        # handle rings
        for dy in [w*0.5, -w*0.5]:
            ring = Circle((cx - w*0.65, cy + dy), w*0.22,
                          color='none', ec='white', lw=2.0, zorder=12)
            ax.add_patch(ring)

    elif idx == 2:  # needle & thread (simplified)
        # needle
        ax.plot([cx - w*0.55, cx + w*0.55], [cy + w*0.4, cy - w*0.4],
                color='white', lw=2.5, solid_capstyle='round', zorder=12)
        # eye of needle
        ey = Circle((cx + w*0.5, cy - w*0.36), w*0.14,
                    color=col, ec='white', lw=1.5, zorder=13)
        ax.add_patch(ey)
        # thread wave
        xs = np.linspace(cx - w*0.5, cx + w*0.3, 40)
        ys = cy - w*0.6 + 0.18 * np.sin(np.linspace(0, 4*np.pi, 40))
        ax.plot(xs, ys, color='white', lw=1.8, alpha=0.85, zorder=12)

    elif idx == 3:  # water drop
        from matplotlib.path import Path
        import matplotlib.patches as mpatch
        verts = [(cx, cy + w*0.75),
                 (cx + w*0.55, cy - w*0.05),
                 (cx + w*0.32, cy - w*0.65),
                 (cx - w*0.32, cy - w*0.65),
                 (cx - w*0.55, cy - w*0.05),
                 (cx, cy + w*0.75)]
        codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4,
                 Path.CURVE4, Path.CURVE4, Path.CLOSEPOLY]
        # simple ellipse instead
        drop = Ellipse((cx, cy - w*0.1), w*1.1, w*1.5,
                       color='white', alpha=0.9, zorder=12)
        ax.add_patch(drop)
        # shine
        shine = Ellipse((cx - w*0.2, cy + w*0.2), w*0.28, w*0.18,
                        color=col, alpha=0.6, zorder=13)
        ax.add_patch(shine)
        # tip
        ax.plot([cx, cx], [cy + w*0.55, cy + w*0.8],
                color='white', lw=2, solid_capstyle='round', zorder=12)

    elif idx == 4:  # wrench
        ax.plot([cx - w*0.5, cx + w*0.5], [cy + w*0.5, cy - w*0.5],
                color='white', lw=4, solid_capstyle='round', zorder=12)
        for dx, dy in [(-w*0.45, w*0.45), (w*0.45, -w*0.45)]:
            head = Circle((cx + dx, cy + dy), w*0.28,
                          color='none', ec='white', lw=2.2, zorder=12)
            ax.add_patch(head)

    elif idx == 5:  # tent (triangle + door)
        # tent body
        tri_x = [cx, cx - w*0.8, cx + w*0.8, cx]
        tri_y = [cy + w*0.75, cy - w*0.45, cy - w*0.45, cy + w*0.75]
        ax.fill(tri_x, tri_y, color='white', alpha=0.9, zorder=12)
        # door arch
        door = Wedge((cx, cy - w*0.45), w*0.28, 0, 180,
                     color=col, zorder=13)
        ax.add_patch(door)
        # ground line
        ax.plot([cx - w*0.85, cx + w*0.85], [cy - w*0.45, cy - w*0.45],
                color='white', lw=2, zorder=12)

    elif idx == 6:  # checkmark in shield
        shield = FancyBboxPatch((cx - w*0.55, cy - w*0.65), w*1.1, w*1.2,
                                boxstyle='round,pad=0.1',
                                color='white', alpha=0.9, zorder=12)
        ax.add_patch(shield)
        # check mark
        ax.plot([cx - w*0.3, cx - w*0.02, cx + w*0.4],
                [cy - w*0.05, cy - w*0.38, cy + w*0.35],
                color=col, lw=3.5, solid_capstyle='round',
                solid_joinstyle='round', zorder=13)

    elif idx == 7:  # box / package
        # box body
        box = FancyBboxPatch((cx - w*0.55, cy - w*0.55), w*1.1, w*1.0,
                             boxstyle='round,pad=0.05',
                             color='white', alpha=0.9, zorder=12)
        ax.add_patch(box)
        # lid flaps
        ax.fill([cx - w*0.55, cx - w*0.55, cx, cx],
                [cy + w*0.45, cy + w*0.68, cy + w*0.68, cy + w*0.45],
                color='white', alpha=0.75, zorder=12)
        ax.fill([cx, cx, cx + w*0.55, cx + w*0.55],
                [cy + w*0.45, cy + w*0.68, cy + w*0.68, cy + w*0.45],
                color='white', alpha=0.6, zorder=12)
        ax.plot([cx - w*0.55, cx + w*0.55], [cy + w*0.45, cy + w*0.45],
                color=col, lw=1.5, zorder=13)
        # ribbon
        ax.plot([cx, cx], [cy - w*0.55, cy + w*0.45],
                color=col, lw=2.0, zorder=13)

    elif idx == 8:  # ship / truck arrow
        # truck body
        truck = FancyBboxPatch((cx - w*0.65, cy - w*0.25), w*1.0, w*0.65,
                               boxstyle='round,pad=0.06',
                               color='white', alpha=0.9, zorder=12)
        ax.add_patch(truck)
        # cabin
        cabin = FancyBboxPatch((cx + w*0.35, cy - w*0.05), w*0.35, w*0.45,
                               boxstyle='round,pad=0.04',
                               color='white', alpha=0.75, zorder=12)
        ax.add_patch(cabin)
        # wheels
        for wx in [cx - w*0.35, cx + w*0.2]:
            wh = Circle((wx, cy - w*0.38), w*0.2, color=col, zorder=13)
            ax.add_patch(wh)
            wh2 = Circle((wx, cy - w*0.38), w*0.1, color='white', zorder=14)
            ax.add_patch(wh2)
        # arrow
        ax.annotate('', xy=(cx + w*0.92, cy + w*0.3),
                    xytext=(cx + w*0.55, cy + w*0.3),
                    arrowprops=dict(arrowstyle='->', color='white', lw=2.0,
                                   mutation_scale=14), zorder=13)

# ═══════════════════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════════════════
header = FancyBboxPatch((0.3, 11.1), 27.4, 1.65,
                         boxstyle='round,pad=0.12',
                         linewidth=0, facecolor='#1C3A4A', zorder=1)
ax.add_patch(header)

# accent bar
ax.add_patch(FancyBboxPatch((0.3, 11.1), 0.55, 1.65,
                             boxstyle='round,pad=0',
                             linewidth=0, facecolor='#E05C2A', zorder=2))
ax.add_patch(FancyBboxPatch((0.85, 11.1), 0.3, 1.65,
                             boxstyle='round,pad=0',
                             linewidth=0, facecolor='#F0A800', zorder=2))
ax.add_patch(FancyBboxPatch((1.15, 11.1), 0.2, 1.65,
                             boxstyle='round,pad=0',
                             linewidth=0, facecolor='#27AE60', zorder=2))

ax.text(14, 12.14, "TENT  MANUFACTURING  PROCESS  FLOW",
        fontsize=27, fontweight='bold', color='#FFFFFF',
        ha='center', va='center', fontfamily='DejaVu Sans', zorder=3)
ax.text(14, 11.52, "From Raw Materials to Finished Product   |   9 Key Production Stages",
        fontsize=12, color='#7EC8E3',
        ha='center', va='center', fontfamily='DejaVu Sans', zorder=3)

# ═══════════════════════════════════════════════════════════════════════════
# CONVEYOR BELT
# ═══════════════════════════════════════════════════════════════════════════
# belt shadow
ax.add_patch(FancyBboxPatch((ML - 0.08, BELT_Y - 0.08), TW + 0.16, BELT_H + 0.08,
                             boxstyle='round,pad=0.1',
                             linewidth=0, facecolor='#000', alpha=0.4, zorder=2))
# belt body
ax.add_patch(FancyBboxPatch((ML - 0.05, BELT_Y), TW + 0.1, BELT_H,
                             boxstyle='round,pad=0.08',
                             linewidth=0, facecolor='#2D4A5A', zorder=3))
# belt top stripe
ax.add_patch(Rectangle((ML, BELT_Y + BELT_H - 0.12), TW, 0.12,
                         color='#3D6070', zorder=4))
# belt ribs
x_rib = ML + 0.25
while x_rib < ML + TW - 0.2:
    ax.add_patch(Rectangle((x_rib, BELT_Y + 0.06), 0.22, BELT_H - 0.12,
                             color='#3D6070', zorder=4))
    x_rib += 0.52

# rollers
for rx in [ML - 0.05, ML + TW + 0.05]:
    ax.add_patch(Circle((rx, BELT_Y + BELT_H/2), BELT_H/2 + 0.1,
                        color='#1C3A4A', zorder=4))
    ax.add_patch(Circle((rx, BELT_Y + BELT_H/2), BELT_H/2 + 0.1,
                        color='none', ec='#4A7A90', lw=2.5, zorder=5))

# ═══════════════════════════════════════════════════════════════════════════
# STEP CARDS
# ═══════════════════════════════════════════════════════════════════════════
for i, (num, title, desc) in enumerate(steps):
    col = STEP_COLORS[i]
    cx  = ML + i * SW + SW / 2
    cx_card = cx - CW / 2

    # shadow
    ax.add_patch(FancyBboxPatch((cx_card + 0.08, CARD_BY - 0.08), CW, CH,
                                boxstyle='round,pad=0.1',
                                linewidth=0, facecolor='#000', alpha=0.38, zorder=4))

    # card body
    ax.add_patch(FancyBboxPatch((cx_card, CARD_BY), CW, CH,
                                boxstyle='round,pad=0.1',
                                linewidth=2.0, edgecolor=col,
                                facecolor='#1C3A4A', zorder=5))

    # top color stripe
    ax.add_patch(FancyBboxPatch((cx_card, CARD_BY + CH - 0.42), CW, 0.55,
                                boxstyle='round,pad=0.1',
                                linewidth=0, facecolor=col, zorder=6))
    ax.add_patch(Rectangle((cx_card, CARD_BY + CH - 0.42), CW, 0.28,
                            color=col, zorder=6))

    # step-number badge (top-right corner)
    ax.add_patch(Circle((cx_card + CW - 0.32, CARD_BY + CH - 0.32), 0.3,
                        color='#12232E', zorder=7))
    ax.text(cx_card + CW - 0.32, CARD_BY + CH - 0.32, num,
            fontsize=8.5, fontweight='bold', color=col,
            ha='center', va='center', zorder=8)

    # icon circle: glow → white ring → colored fill
    ax.add_patch(Circle((cx, ICON_CY), ICON_R + 0.18, color=col, alpha=0.18, zorder=6))
    ax.add_patch(Circle((cx, ICON_CY), ICON_R + 0.07, color='white', zorder=7))
    ax.add_patch(Circle((cx, ICON_CY), ICON_R, color=col, zorder=8))

    # vector icon
    draw_icon(ax, i, cx, ICON_CY, ICON_R, col)

    # title
    title_y = ICON_CY - ICON_R - 0.38
    ax.text(cx, title_y, title,
            fontsize=9.5, fontweight='bold', color='#FFFFFF',
            ha='center', va='top', linespacing=1.55, zorder=9)

    # desc
    ax.text(cx, title_y - 1.15, desc,
            fontsize=8.2, color='#90B8C8',
            ha='center', va='top', linespacing=1.6, zorder=9)

    # colored bottom accent bar
    ax.add_patch(Rectangle((cx_card + 0.15, CARD_BY + 0.12), CW - 0.30, 0.1,
                            color=col, alpha=0.5, zorder=6))

    # arrow to next card
    if i < N - 1:
        arr_xs = cx_card + CW + 0.05
        arr_xe = cx_card + SW - 0.05
        arr_y  = CARD_BY + CH * 0.5
        ax.annotate('', xy=(arr_xe, arr_y), xytext=(arr_xs, arr_y),
                    arrowprops=dict(arrowstyle='->', color=col,
                                   lw=2.4, mutation_scale=16), zorder=10)

# ═══════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════
ax.add_patch(FancyBboxPatch((0.3, 0.18), 27.4, 0.95,
                             boxstyle='round,pad=0.08',
                             linewidth=0, facecolor='#1C3A4A', zorder=2))
ax.text(14, 0.65,
        "Professional Outdoor Gear Manufacturing   ·   Strict Quality at Every Stage   ·   World-Class Tent Production",
        fontsize=10, color='#7EC8E3',
        ha='center', va='center', style='italic', zorder=3)

# footer color dots
dot_cols = STEP_COLORS[:5]
for j, dc in enumerate(dot_cols):
    ax.add_patch(Circle((1.1 + j * 0.45, 0.65), 0.08, color=dc, zorder=4))
    ax.add_patch(Circle((26.9 - j * 0.45, 0.65), 0.08, color=dc, zorder=4))

# ── Save ──────────────────────────────────────────────────────────────────
plt.tight_layout(pad=0)
out = r'C:\Users\Ray\.accio\accounts\1749967330\agents\DID-F456DA-2B0D4C\project\tent_flow_v2.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor=fig.get_facecolor())
print("Saved:", out)
