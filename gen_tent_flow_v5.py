import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Ellipse, Wedge
import matplotlib.patheffects as pe
import numpy as np

# ══════════════════════════════════════════════════════════════════════════
# CANVAS
# ══════════════════════════════════════════════════════════════════════════
FIG_W, FIG_H = 34, 16
fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
ax.set_xlim(0, FIG_W); ax.set_ylim(0, FIG_H)
ax.axis('off')
BG = '#0D1F2D'
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)

# subtle dot-grid
for gx in np.arange(1, FIG_W, 1.8):
    for gy in np.arange(1, FIG_H, 1.8):
        ax.plot(gx, gy, '.', color='#1A3040', ms=1.2, zorder=0)

STEP_COLORS = [
    "#E8643A","#F0A800","#27AE60","#1E8BC3","#9B59B6",
    "#E8643A","#F0A800","#27AE60","#1E8BC3",
]

steps = [
    ("01","Fabric Weaving\n& Production",
     ["Polyester & Nylon yarns","woven into high-density","base cloth at supplier","mill with strict GSM","& tensile strength ctrl"],
     "Supplier Mill"),
    ("02","Surface Coating\nTreatment",
     ["PU waterproof coating","Flame-retardant finish","UV-blocking treatment","Silver heat-reflective","coat applied at mill"],
     "Done at Mill"),
    ("03","Fabric Cutting\n& Patterning",
     ["Coated rolls received","CNC die-cutting machine","slices precise patterns","Template alignment done","panel by panel check"],
     "In-Factory"),
    ("04","Sewing &\nStitching",
     ["Industrial sewing lines","join all fabric panels","Double-needle seam stitch","Bar-tack reinforcement","at all stress points"],
     "In-Factory"),
    ("05","Pole & Frame\nAssembly",
     ["Fiberglass & aluminum","poles cut to length","Shock-cord threaded through","each pole section","Ferrule caps installed"],
     "In-Factory"),
    ("06","Component\nIntegration",
     ["Tent body & flysheet","assembled onto frame","Guy lines attached","Ground stakes packed in","Zippers tested & lubed"],
     "In-Factory"),
    ("07","Quality Control\n& Testing",
     ["Hydrostatic water-column","pressure resistance test","Wind tunnel load simulation","All seams integrity scan","Pass / fail logged by QC"],
     "QC Lab"),
    ("08","Packaging\n& Labeling",
     ["Tent folded & rolled","packed into carry bag","Care & spec label applied","Barcode & QR code stuck","Master carton sealed"],
     "In-Factory"),
    ("09","Warehousing\n& Shipping",
     ["Inventory logged in WMS","Orders picked & palletized","Export docs & packing list","Container stuffing done","Delivered worldwide"],
     "Warehouse"),
]
N = len(steps)

# ══════════════════════════════════════════════════════════════════════════
# LAYOUT — cards stretch from near-top to near-bottom
# ══════════════════════════════════════════════════════════════════════════
HEADER_H  = 1.92        # header height
HEADER_Y  = FIG_H - HEADER_H - 0.18   # 13.90
FOOTER_H  = 0.90
FOOTER_Y  = 0.12

CARD_BY   = FOOTER_Y + FOOTER_H + 0.22   # 1.24  — card bottom
CARD_TY   = HEADER_Y - 0.22              # 13.68 — card top
CARD_H    = CARD_TY - CARD_BY            # ≈ 12.44  ← very tall

PAD_L, PAD_R = 0.50, 0.50
TOTAL_W   = FIG_W - PAD_L - PAD_R        # 33.0
STEP_W    = TOTAL_W / N                  # 3.67
CARD_W    = STEP_W * 0.87               # 3.19

ICON_R    = 1.28                         # large icon circle
# icon circle sits high — top 25% of card
ICON_CY   = CARD_BY + CARD_H * 0.83

# belt drawn across the icon horizontal band
BELT_Y    = ICON_CY - 0.42
BELT_H    = 0.84

# ══════════════════════════════════════════════════════════════════════════
# VECTOR ICONS
# ══════════════════════════════════════════════════════════════════════════
def draw_icon(ax, idx, cx, cy, r, col):
    s = r * 0.66

    if idx == 0:   # weave grid
        for xi in np.linspace(cx-s*.75, cx+s*.75, 6):
            ax.plot([xi,xi],[cy-s*.80,cy+s*.80],color='white',lw=2.0,alpha=.85,zorder=13)
        for yi in np.linspace(cy-s*.65, cy+s*.65, 5):
            ax.plot([cx-s*.78,cx+s*.78],[yi,yi],color='#FFD580',lw=2.6,alpha=.95,zorder=14)
        ax.add_patch(FancyBboxPatch((cx-s*.78,cy+s*.58),s*1.56,s*.32,
            boxstyle='round,pad=0.04',color=col,ec='white',lw=1.2,zorder=15))

    elif idx == 1:  # paint roller
        ax.plot([cx-s*.6,cx+s*.12],[cy+s*.75,cy+s*.05],color='white',lw=3.2,
                solid_capstyle='round',zorder=13)
        ax.add_patch(FancyBboxPatch((cx-s*.18,cy-s*.58),s*.82,s*.44,
            boxstyle='round,pad=0.07',color='white',zorder=13))
        for ci,cc in enumerate(['#E8643A','#F0A800','#27AE60','#1E8BC3']):
            ax.add_patch(Rectangle((cx-s*.16+ci*s*.18,cy-s*.56),s*.15,s*.40,color=cc,zorder=14))
        for dp,dy_off in [(cx+s*.05,-.25),(cx+s*.32,-.40),(cx+s*.55,-.22)]:
            ax.add_patch(Ellipse((dp,cy-s*.95+dy_off),s*.16,s*.32,color=col,alpha=.85,zorder=14))

    elif idx == 2:  # scissors + fabric
        fx=[cx-s*.75,cx+s*.12,cx+s*.75,cx-s*.12,cx-s*.75]
        fy=[cy-s*.32,cy-s*.32,cy+s*.32,cy+s*.32,cy-s*.32]
        ax.fill(fx,fy,color='white',alpha=.15,zorder=12)
        ax.plot(fx,fy,color='white',lw=1.4,alpha=.55,zorder=13)
        ax.plot([cx-s*.75,cx+s*.75],[cy,cy],color='#FFD580',lw=2.2,ls='--',dashes=(5,3),zorder=13)
        for sign in [1,-1]:
            ax.plot([cx+s*.02,cx+s*.78],[cy,cy+sign*s*.60],color='white',lw=3.2,
                    solid_capstyle='round',zorder=14)
            ax.add_patch(Circle((cx-s*.20,cy+sign*s*.24),s*.24,
                                color='none',ec='white',lw=2.4,zorder=14))
        ax.add_patch(Circle((cx,cy),s*.14,color=col,zorder=15))

    elif idx == 3:  # sewing machine
        ax.add_patch(FancyBboxPatch((cx-s*.78,cy-s*.58),s*1.18,s*.80,
            boxstyle='round,pad=0.09',color='white',alpha=.90,zorder=12))
        ax.add_patch(FancyBboxPatch((cx-s*.60,cy+s*.22),s*.98,s*.36,
            boxstyle='round,pad=0.07',color='white',alpha=.72,zorder=12))
        ax.plot([cx+s*.30,cx+s*.30],[cy+s*.22,cy-s*.58],color=col,lw=2.8,zorder=13)
        ax.add_patch(Ellipse((cx+s*.30,cy-s*.58),s*.12,s*.18,color='#FFD580',zorder=14))
        for xi in np.linspace(cx-s*.62,cx+s*.52,9):
            ax.add_patch(Rectangle((xi,cy-s*.76),s*.08,s*.14,color='#FFD580',zorder=13))
        ax.add_patch(Circle((cx-s*.44,cy+s*.40),s*.28,color=col,ec='white',lw=1.8,zorder=13))
        ax.add_patch(Circle((cx-s*.44,cy+s*.40),s*.11,color='white',zorder=14))

    elif idx == 4:  # tent pole
        ax.plot([cx-s*.70,cx+s*.70],[cy-s*.65,cy+s*.65],color='white',lw=6.0,
                solid_capstyle='round',
                path_effects=[pe.withStroke(linewidth=8,foreground=col)],zorder=12)
        ax.plot([cx-s*.55,cx+s*.55],[cy+s*.45,cy-s*.55],color='#B0C8D8',lw=4.5,
                solid_capstyle='round',zorder=12)
        cx2=np.linspace(cx-s*.35,cx+s*.35,32)
        cy2=cy+s*.06+s*.14*np.sin(np.linspace(0,6*np.pi,32))
        ax.plot(cx2,cy2,color='#FFD580',lw=2.2,zorder=13)
        for ex,ey in [(cx-s*.70,cy-s*.65),(cx+s*.70,cy+s*.65)]:
            ax.add_patch(Circle((ex,ey),s*.14,color=col,ec='white',lw=1.4,zorder=14))

    elif idx == 5:  # full tent
        ax.add_patch(Ellipse((cx,cy-s*.78),s*1.72,s*.24,color='#000',alpha=.22,zorder=11))
        fly_x=[cx-s*.95,cx,cx+s*.95,cx+s*.62,cx-s*.62,cx-s*.95]
        fly_y=[cy-s*.65,cy+s*.88,cy-s*.65,cy-s*.65,cy-s*.65,cy-s*.65]
        ax.fill(fly_x,fly_y,color='#4A7FA5',alpha=.72,zorder=12)
        ax.plot([cx-s*.95,cx,cx+s*.95],[cy-s*.65,cy+s*.88,cy-s*.65],
                color='white',lw=2.5,zorder=13)
        in_x=[cx-s*.58,cx,cx+s*.58]; in_y=[cy-s*.58,cy+s*.48,cy-s*.58]
        ax.fill(in_x,in_y,color='white',alpha=.22,zorder=13)
        ax.add_patch(Wedge((cx,cy-s*.58),s*.30,0,180,color=col,alpha=.92,zorder=14))
        for gx_off,gy_off in [(-s*.95,-s*.65),(s*.95,-s*.65)]:
            ax.plot([cx+gx_off*.72,cx+gx_off*1.20],[cy-s*.22,cy+gy_off*.90],
                    color='#FFD580',lw=1.8,ls='--',zorder=13)
        for sx_off in [-s*1.18,s*1.18]:
            ax.plot([cx+sx_off,cx+sx_off],[cy-s*.80,cy-s*.62],
                    color='#B0C8D8',lw=2.8,solid_capstyle='round',zorder=13)

    elif idx == 6:  # QC shield
        sh_x=[cx,cx+s*.68,cx+s*.68,cx,cx-s*.68,cx-s*.68,cx]
        sh_y=[cy+s*.88,cy+s*.48,cy-s*.18,cy-s*.85,cy-s*.18,cy+s*.48,cy+s*.88]
        ax.fill(sh_x,sh_y,color='white',alpha=.16,zorder=12)
        ax.plot(sh_x,sh_y,color='white',lw=2.5,zorder=13)
        ax.plot([cx-s*.35,cx-s*.02,cx+s*.45],[cy-s*.04,cy-s*.40,cy+s*.48],
                color=col,lw=5.0,solid_capstyle='round',solid_joinstyle='round',zorder=14)
        ax.text(cx,cy-s*.65,'QC',fontsize=9,fontweight='bold',
                color='white',ha='center',va='center',zorder=14)

    elif idx == 7:  # open box
        ax.add_patch(FancyBboxPatch((cx-s*.70,cy-s*.70),s*1.40,s*1.12,
            boxstyle='round,pad=0.07',color='white',alpha=.86,zorder=12))
        ax.fill([cx-s*.70,cx-s*.70,cx,cx],[cy+s*.42,cy+s*.75,cy+s*.75,cy+s*.42],
                color='white',alpha=.58,zorder=12)
        ax.fill([cx,cx,cx+s*.70,cx+s*.70],[cy+s*.42,cy+s*.75,cy+s*.75,cy+s*.42],
                color='white',alpha=.44,zorder=12)
        ax.plot([cx-s*.70,cx+s*.70],[cy+s*.42,cy+s*.42],color=col,lw=2.0,zorder=13)
        ax.plot([cx,cx],[cy-s*.70,cy+s*.42],color=col,lw=2.8,zorder=13)
        ax.plot([cx-s*.70,cx+s*.70],[cy-s*.10,cy-s*.10],color=col,lw=2.8,zorder=13)
        ax.add_patch(FancyBboxPatch((cx-s*.45,cy-s*.60),s*.90,s*.38,
            boxstyle='round,pad=0.05',color=col,alpha=.78,zorder=14))
        ax.text(cx,cy-s*.41,'LABEL',fontsize=7,fontweight='bold',
                color='white',ha='center',va='center',zorder=15)

    elif idx == 8:  # cargo ship
        for wy in [cy-s*.68,cy-s*.54]:
            wx=np.linspace(cx-s*.95,cx+s*.95,42)
            wy2=wy+s*.06*np.sin(np.linspace(0,4*np.pi,42))
            ax.plot(wx,wy2,color='#4A90D9',lw=2.2,alpha=.72,zorder=11)
        hull_x=[cx-s*.90,cx-s*.95,cx+s*.95,cx+s*.90,cx-s*.90]
        hull_y=[cy-s*.44,cy-s*.66,cy-s*.66,cy-s*.44,cy-s*.44]
        ax.fill(hull_x,hull_y,color='#2C3E50',zorder=12)
        ax.add_patch(FancyBboxPatch((cx-s*.88,cy-s*.44),s*1.76,s*.38,
            boxstyle='round,pad=0.04',color='#ECF0F1',alpha=.90,zorder=12))
        for ci,cc in enumerate(['#E8643A','#1E8BC3','#27AE60','#F0A800','#9B59B6','#E8643A']):
            ax.add_patch(Rectangle((cx-s*.82+ci*s*.28,cy-s*.38),s*.24,s*.28,color=cc,zorder=13))
        ax.add_patch(FancyBboxPatch((cx+s*.46,cy-s*.06),s*.40,s*.56,
            boxstyle='round,pad=0.04',color='#2C3E50',zorder=13))
        for wy3 in [cy+s*.24,cy+s*.07]:
            ax.add_patch(Rectangle((cx+s*.54,wy3),s*.12,s*.12,color='#FFD580',zorder=14))
        smk_x=np.linspace(cx+s*.62,cx+s*.46,14)
        smk_y=np.linspace(cy+s*.52,cy+s*.90,14)
        ax.plot(smk_x+s*.10*np.sin(np.linspace(0,3,14)),smk_y,
                color='#B0C8D8',lw=2.8,alpha=.55,zorder=13)


# ══════════════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════════════
ax.add_patch(FancyBboxPatch((0.28, HEADER_Y), FIG_W-0.56, HEADER_H,
    boxstyle='round,pad=0.10', linewidth=0, facecolor='#162533', zorder=1))
# accent bars
for xi,col in [(0.28,'#E8643A'),(0.88,'#F0A800'),(1.36,'#27AE60'),(1.74,'#1E8BC3')]:
    ax.add_patch(Rectangle((xi, HEADER_Y), 0.44, HEADER_H, color=col, zorder=2))

ax.text(FIG_W/2, HEADER_Y+HEADER_H*0.68,
        "TENT  MANUFACTURING  PROCESS  FLOW",
        fontsize=34, fontweight='bold', color='#FFFFFF',
        ha='center', va='center', fontfamily='DejaVu Sans', zorder=3)
ax.text(FIG_W/2, HEADER_Y+HEADER_H*0.22,
        "Corrected Production Sequence  ·  From Raw Fabric to Finished Tent  ·  9 Key Stages",
        fontsize=14, color='#7EC8E3',
        ha='center', va='center', fontfamily='DejaVu Sans', zorder=3)

# ══════════════════════════════════════════════════════════════════════════
# CONVEYOR BELT
# ══════════════════════════════════════════════════════════════════════════
ax.add_patch(FancyBboxPatch((PAD_L-0.10, BELT_Y), TOTAL_W+0.20, BELT_H,
    boxstyle='round,pad=0.08', linewidth=0, facecolor='#1E3A4A', zorder=2))
xr = PAD_L+0.18
while xr < PAD_L+TOTAL_W-0.15:
    ax.add_patch(Rectangle((xr, BELT_Y+0.08), 0.28, BELT_H-0.16, color='#2A4A5A', zorder=3))
    xr += 0.58
ax.plot([PAD_L, PAD_L+TOTAL_W],[BELT_Y+BELT_H-0.06]*2, color='#3D6070', lw=2, zorder=4)
for rx in [PAD_L-0.10, PAD_L+TOTAL_W+0.10]:
    ax.add_patch(Circle((rx, BELT_Y+BELT_H/2), BELT_H/2+0.14, color='#1C3A4A', zorder=4))
    ax.add_patch(Circle((rx, BELT_Y+BELT_H/2), BELT_H/2+0.14,
                        color='none', ec='#4A7A90', lw=2.8, zorder=5))

# ══════════════════════════════════════════════════════════════════════════
# CARDS
# ══════════════════════════════════════════════════════════════════════════
for i,(num,title,desc,note) in enumerate(steps):
    col = STEP_COLORS[i]
    cx  = PAD_L + i*STEP_W + STEP_W/2
    card_x = cx - CARD_W/2

    # shadow
    ax.add_patch(FancyBboxPatch((card_x+0.10, CARD_BY-0.10), CARD_W, CARD_H,
        boxstyle='round,pad=0.12', linewidth=0, facecolor='#000', alpha=0.42, zorder=4))
    # card body
    ax.add_patch(FancyBboxPatch((card_x, CARD_BY), CARD_W, CARD_H,
        boxstyle='round,pad=0.12', linewidth=2.5, edgecolor=col,
        facecolor='#162533', zorder=5))
    # top color bar
    bar_h = 0.58
    ax.add_patch(FancyBboxPatch((card_x, CARD_BY+CARD_H-bar_h), CARD_W, bar_h+0.12,
        boxstyle='round,pad=0.12', linewidth=0, facecolor=col, zorder=6))
    ax.add_patch(Rectangle((card_x, CARD_BY+CARD_H-bar_h), CARD_W, bar_h*0.5,
        color=col, zorder=6))

    # step number badge
    ax.add_patch(Circle((card_x+CARD_W-0.40, CARD_BY+CARD_H-0.40), 0.36,
                        color='#0D1F2D', zorder=7))
    ax.text(card_x+CARD_W-0.40, CARD_BY+CARD_H-0.40, num,
            fontsize=11, fontweight='bold', color=col,
            ha='center', va='center', zorder=8)

    # location tag
    tag_col = '#E05C2A' if 'Mill' in note or 'Supplier' in note else \
              '#F0A800' if 'QC' in note or 'Ware' in note else '#27AE60'
    ax.add_patch(FancyBboxPatch((card_x+0.14, CARD_BY+CARD_H-1.50), CARD_W-0.28, 0.38,
        boxstyle='round,pad=0.05', linewidth=0, facecolor=tag_col, alpha=0.20, zorder=7))
    ax.text(cx, CARD_BY+CARD_H-1.30, note,
            fontsize=10, color=tag_col, fontweight='bold',
            ha='center', va='center', zorder=8)

    # icon circle
    ax.add_patch(Circle((cx, ICON_CY), ICON_R+0.28, color=col, alpha=0.14, zorder=6))
    ax.add_patch(Circle((cx, ICON_CY), ICON_R+0.10, color='white', zorder=7))
    ax.add_patch(Circle((cx, ICON_CY), ICON_R, color=col, zorder=8))
    draw_icon(ax, i, cx, ICON_CY, ICON_R, col)

    # ── TEXT: title then desc lines, evenly spaced to fill card bottom ───
    text_top    = ICON_CY - ICON_R - 0.28   # just below icon
    text_bottom = CARD_BY + 0.30             # just above card bottom

    # title = 2 lines bold
    title_lines = title.split('\n')
    n_title = len(title_lines)
    n_desc  = len(desc)
    n_total = n_title + n_desc          # total lines = 2 + 5 = 7

    # distribute evenly: step = total height / (n_total - 1)
    total_h = text_top - text_bottom
    step    = total_h / (n_total - 1)

    for li, line in enumerate(title_lines):
        y = text_top - li * step
        ax.text(cx, y, line,
                fontsize=17, fontweight='bold', color='#FFFFFF',
                ha='center', va='center', zorder=9)

    for di, line in enumerate(desc):
        y = text_top - (n_title + di) * step
        ax.text(cx, y, line,
                fontsize=15, color='#90B8C8',
                ha='center', va='center', zorder=9)

    # bottom accent line
    ax.add_patch(Rectangle((card_x+0.20, CARD_BY+0.18), CARD_W-0.40, 0.10,
                            color=col, alpha=0.45, zorder=6))

    # connector arrow
    if i < N-1:
        ax_s = card_x + CARD_W + 0.06
        ax_e = card_x + STEP_W - 0.06
        a_y  = ICON_CY
        ax.annotate('', xy=(ax_e, a_y), xytext=(ax_s, a_y),
                    arrowprops=dict(arrowstyle='->', color=col,
                                   lw=2.8, mutation_scale=20), zorder=10)

    # (divider removed)

# ══════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════
ax.add_patch(FancyBboxPatch((0.28, FOOTER_Y), FIG_W-0.56, FOOTER_H,
    boxstyle='round,pad=0.08', linewidth=0, facecolor='#162533', zorder=2))
ax.text(FIG_W/2, FOOTER_Y+FOOTER_H/2,
        "Professional Outdoor Gear Manufacturing   ·   Strict Quality Control at Every Stage   ·   World-Class Tent Production",
        fontsize=12, color='#7EC8E3', ha='center', va='center', style='italic', zorder=3)
for j,dc in enumerate(["#E8643A","#F0A800","#27AE60","#1E8BC3","#9B59B6"]):
    ax.add_patch(Circle((1.2+j*0.55, FOOTER_Y+FOOTER_H/2), 0.10, color=dc, zorder=4))
    ax.add_patch(Circle((FIG_W-1.2-j*0.55, FOOTER_Y+FOOTER_H/2), 0.10, color=dc, zorder=4))

# ══════════════════════════════════════════════════════════════════════════
# SAVE
# ══════════════════════════════════════════════════════════════════════════
plt.tight_layout(pad=0)
out = r'C:\Users\Ray\.accio\accounts\1749967330\agents\DID-F456DA-2B0D4C\project\tent_flow_v8.png'
plt.savefig(out, dpi=170, bbox_inches='tight', facecolor=fig.get_facecolor())
print("Saved:", out)
