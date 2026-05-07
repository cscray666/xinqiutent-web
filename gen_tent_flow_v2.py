import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Arc, Circle, Wedge
import matplotlib.patheffects as pe
import numpy as np

# ── Canvas ──────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(26, 14))
ax.set_xlim(0, 26)
ax.set_ylim(0, 14)
ax.axis('off')
fig.patch.set_facecolor('#1A2A3A')
ax.set_facecolor('#1A2A3A')

# ── Step data ────────────────────────────────────────────────────────────
steps = [
    {
        "title":    "Raw Material\nInspection",
        "desc":     "Fabric · Poles\nZippers · Buckles",
        "color":    "#E8643A",
        "icon":     "🔍",
        "num":      "01",
    },
    {
        "title":    "Fabric Cutting\n& Patterning",
        "desc":     "CNC Cutting\nTemplate Matching",
        "color":    "#F0A500",
        "icon":     "✂️",
        "num":      "02",
    },
    {
        "title":    "Sewing &\nStitching",
        "desc":     "Industrial Sewing\nSeam Reinforcement",
        "color":    "#4CAF7D",
        "icon":     "🧵",
        "num":      "03",
    },
    {
        "title":    "Waterproofing\n& Coating",
        "desc":     "PU Coating\nHeat-Seal Seams",
        "color":    "#2196C4",
        "icon":     "💧",
        "num":      "04",
    },
    {
        "title":    "Pole & Frame\nAssembly",
        "desc":     "Fiberglass Poles\nShock Cord Rigging",
        "color":    "#9C5FB5",
        "icon":     "🔧",
        "num":      "05",
    },
    {
        "title":    "Component\nIntegration",
        "desc":     "Flysheet · Stakes\nGuy Lines",
        "color":    "#E8643A",
        "icon":     "⛺",
        "num":      "06",
    },
    {
        "title":    "Quality Control\n& Testing",
        "desc":     "Water · Load\nWind Resistance",
        "color":    "#F0A500",
        "icon":     "✅",
        "num":      "07",
    },
    {
        "title":    "Packaging\n& Labeling",
        "desc":     "Folding · Bagging\nBarcode Labels",
        "color":    "#4CAF7D",
        "icon":     "📦",
        "num":      "08",
    },
    {
        "title":    "Warehousing\n& Shipping",
        "desc":     "Inventory Mgmt\nExport & Delivery",
        "color":    "#2196C4",
        "icon":     "🚢",
        "num":      "09",
    },
]

N = len(steps)

# ── Layout constants ─────────────────────────────────────────────────────
MARGIN_L    = 0.9
MARGIN_R    = 0.9
TOTAL_W     = 26 - MARGIN_L - MARGIN_R
STEP_W      = TOTAL_W / N          # ≈ 2.69
CARD_W      = STEP_W * 0.82
CARD_H      = 7.2
BELT_Y      = 3.8                  # top of the conveyor belt
BELT_H      = 0.55
CARD_BOT_Y  = BELT_Y + BELT_H
CARD_TOP_Y  = CARD_BOT_Y + CARD_H
ICON_R      = 0.72                 # radius of icon circle
ICON_CY     = CARD_TOP_Y - ICON_R - 0.25

# ── Header ────────────────────────────────────────────────────────────────
header_box = FancyBboxPatch((0.4, 11.5), 25.2, 2.1,
                             boxstyle='round,pad=0.12',
                             linewidth=0, facecolor='#243B55', zorder=1)
ax.add_patch(header_box)

ax.text(13, 12.85,
        "TENT  MANUFACTURING  PROCESS  FLOW",
        fontsize=26, fontweight='bold', color='#FFFFFF',
        ha='center', va='center', fontfamily='DejaVu Sans',
        zorder=2)
ax.text(13, 12.2,
        "From Raw Materials to Finished Product  |  9 Key Production Stages",
        fontsize=13, color='#90CAF9',
        ha='center', va='center', fontfamily='DejaVu Sans',
        zorder=2)

# decorative accent lines on header
for xp, col in [(0.6,'#E8643A'),(1.1,'#F0A500'),(1.6,'#4CAF7D'),(2.1,'#2196C4')]:
    ax.plot([xp, xp], [11.55, 13.55], color=col, linewidth=5, solid_capstyle='round', zorder=3)

# ── Conveyor belt ─────────────────────────────────────────────────────────
# belt background
belt_bg = FancyBboxPatch((MARGIN_L - 0.1, BELT_Y), TOTAL_W + 0.2, BELT_H,
                          boxstyle='round,pad=0.08',
                          linewidth=0, facecolor='#37474F', zorder=2)
ax.add_patch(belt_bg)

# belt stripes (dashes)
stripe_w = 0.35
gap_w    = 0.28
x_s = MARGIN_L + 0.1
while x_s + stripe_w < 26 - MARGIN_R:
    stripe = FancyBboxPatch((x_s, BELT_Y + 0.06), stripe_w, BELT_H - 0.12,
                             boxstyle='round,pad=0.03',
                             linewidth=0, facecolor='#546E7A', zorder=3)
    ax.add_patch(stripe)
    x_s += stripe_w + gap_w

# belt top/bottom edges
for yy in [BELT_Y + 0.04, BELT_Y + BELT_H - 0.04]:
    ax.plot([MARGIN_L - 0.05, 26 - MARGIN_R + 0.05], [yy, yy],
            color='#607D8B', linewidth=2, zorder=4)

# belt rollers at both ends
for rx in [MARGIN_L - 0.05, 26 - MARGIN_R + 0.05]:
    roller = Circle((rx, BELT_Y + BELT_H / 2), BELT_H / 2 + 0.05,
                    color='#455A64', zorder=4)
    ax.add_patch(roller)
    roller_shine = Circle((rx, BELT_Y + BELT_H / 2), BELT_H / 2 + 0.05,
                          color='none', linewidth=2, ec='#78909C', zorder=5)
    ax.add_patch(roller_shine)

# ── Draw each step ────────────────────────────────────────────────────────
for i, step in enumerate(steps):
    cx = MARGIN_L + i * STEP_W + STEP_W / 2   # center x of step
    card_x = cx - CARD_W / 2

    col = step["color"]
    dark_col = col  # accent

    # ── Card shadow ──────────────────────────────────────────────────────
    shadow = FancyBboxPatch((card_x + 0.07, CARD_BOT_Y - 0.07), CARD_W, CARD_H,
                             boxstyle='round,pad=0.1',
                             linewidth=0, facecolor='#000000', alpha=0.35, zorder=4)
    ax.add_patch(shadow)

    # ── Card body ────────────────────────────────────────────────────────
    card = FancyBboxPatch((card_x, CARD_BOT_Y), CARD_W, CARD_H,
                           boxstyle='round,pad=0.1',
                           linewidth=2, edgecolor=col,
                           facecolor='#243B55', zorder=5)
    ax.add_patch(card)

    # colored top stripe
    stripe_h = 0.35
    stripe = FancyBboxPatch((card_x, CARD_BOT_Y + CARD_H - stripe_h), CARD_W, stripe_h + 0.1,
                             boxstyle='round,pad=0.1',
                             linewidth=0, facecolor=col, zorder=6)
    ax.add_patch(stripe)
    # cover the rounded bottom of stripe with a rect
    ax.add_patch(plt.Rectangle((card_x, CARD_BOT_Y + CARD_H - stripe_h),
                                CARD_W, stripe_h * 0.6,
                                color=col, zorder=6))

    # ── Icon circle ──────────────────────────────────────────────────────
    # outer glow ring
    glow = Circle((cx, ICON_CY), ICON_R + 0.12,
                  color=col, alpha=0.25, zorder=6)
    ax.add_patch(glow)
    # white ring
    ring = Circle((cx, ICON_CY), ICON_R + 0.04,
                  color='#FFFFFF', zorder=7)
    ax.add_patch(ring)
    # colored fill
    icon_circ = Circle((cx, ICON_CY), ICON_R,
                        color=col, zorder=8)
    ax.add_patch(icon_circ)
    # icon emoji
    ax.text(cx, ICON_CY, step["icon"],
            fontsize=22, ha='center', va='center', zorder=9)

    # ── Step number badge ────────────────────────────────────────────────
    badge = Circle((card_x + CARD_W - 0.32, CARD_BOT_Y + CARD_H - 0.32), 0.28,
                   color='#1A2A3A', zorder=9)
    ax.add_patch(badge)
    ax.text(card_x + CARD_W - 0.32, CARD_BOT_Y + CARD_H - 0.32,
            step["num"], fontsize=8, fontweight='bold', color=col,
            ha='center', va='center', zorder=10)

    # ── Title ────────────────────────────────────────────────────────────
    title_y = ICON_CY - ICON_R - 0.38
    ax.text(cx, title_y, step["title"],
            fontsize=9.5, fontweight='bold', color='#FFFFFF',
            ha='center', va='top', zorder=9,
            linespacing=1.5)

    # ── Desc ─────────────────────────────────────────────────────────────
    desc_y = title_y - 1.05
    ax.text(cx, desc_y, step["desc"],
            fontsize=7.8, color='#B0BEC5',
            ha='center', va='top', zorder=9,
            linespacing=1.6)

    # ── Connector arrow between cards ────────────────────────────────────
    if i < N - 1:
        arr_x_start = card_x + CARD_W + 0.04
        arr_x_end   = card_x + STEP_W - 0.04
        arr_y       = CARD_BOT_Y + CARD_H * 0.52
        ax.annotate('',
                    xy=(arr_x_end, arr_y),
                    xytext=(arr_x_start, arr_y),
                    arrowprops=dict(
                        arrowstyle='->', color=col,
                        lw=2.2, mutation_scale=16),
                    zorder=10)

# ── Bottom label bar ─────────────────────────────────────────────────────
footer_box = FancyBboxPatch((0.4, 0.25), 25.2, 1.15),
footer_patch = FancyBboxPatch((0.4, 0.25), 25.2, 1.15,
                               boxstyle='round,pad=0.08',
                               linewidth=0, facecolor='#243B55', zorder=2)
ax.add_patch(footer_patch)

ax.text(13, 0.82,
        "Professional Outdoor Gear Manufacturing  ·  Strict Quality at Every Stage  ·  World-Class Tents",
        fontsize=10.5, color='#90CAF9',
        ha='center', va='center', fontfamily='DejaVu Sans',
        style='italic', zorder=3)

# color dots footer accent
dot_colors = ["#E8643A","#F0A500","#4CAF7D","#2196C4","#9C5FB5"]
for j, dc in enumerate(dot_colors):
    ax.add_patch(Circle((1.2 + j * 0.45, 0.82), 0.07, color=dc, zorder=4))
    ax.add_patch(Circle((24.8 - j * 0.45, 0.82), 0.07, color=dc, zorder=4))

# ── Save ─────────────────────────────────────────────────────────────────
plt.tight_layout(pad=0)
out = r'C:\Users\Ray\.accio\accounts\1749967330\agents\DID-F456DA-2B0D4C\project\tent_flow_v2.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor=fig.get_facecolor())
print("Saved:", out)
