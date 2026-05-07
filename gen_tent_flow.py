import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(14, 20))
ax.set_xlim(0, 14)
ax.set_ylim(0, 20)
ax.axis('off')
fig.patch.set_facecolor('#F0F4F0')
ax.set_facecolor('#F0F4F0')

# Color scheme
COLOR_PRIMARY = '#1B5E20'
COLOR_BOX = '#2E7D32'
COLOR_BOX_LIGHT = '#388E3C'
COLOR_ARROW = '#1B5E20'
COLOR_STEP_NUM = '#FFFFFF'
COLOR_TEXT = '#FFFFFF'
COLOR_SUBTITLE = '#81C784'
COLOR_BORDER = '#4CAF50'

# Title
ax.text(7, 19.2, 'Tent Manufacturing Process Flow',
        fontsize=22, fontweight='bold', color=COLOR_PRIMARY,
        ha='center', va='center',
        fontfamily='Arial')
ax.text(7, 18.65, 'From Raw Materials to Finished Product',
        fontsize=12, color='#4CAF50',
        ha='center', va='center',
        fontfamily='Arial')

# Decorative title underline
ax.plot([1.5, 12.5], [18.35, 18.35], color='#4CAF50', linewidth=2.5)

# Steps data: (icon, title, subtitle)
steps = [
    ('01', 'Raw Material Inspection',
     'Fabric · Poles · Zippers · Buckles · Ropes'),
    ('02', 'Fabric Cutting & Pattern Making',
     'CNC Cutting · Template Matching · Precision Trimming'),
    ('03', 'Sewing & Stitching',
     'Industrial Sewing · Seam Reinforcement · Bartacking'),
    ('04', 'Waterproofing & Coating Treatment',
     'PU Coating · Heat-Sealing Seams · UV Protection'),
    ('05', 'Pole & Frame Assembly',
     'Fiberglass / Aluminum Poles · Shock Cord Integration'),
    ('06', 'Component Integration',
     'Tent Body · Flysheet · Stakes · Guy Lines'),
    ('07', 'Quality Control & Testing',
     'Water Resistance · Load Test · Wind Resistance'),
    ('08', 'Packaging & Labeling',
     'Folding · Bag Packing · Barcode & Care Labels'),
    ('09', 'Warehousing & Shipping',
     'Inventory Management · Order Fulfillment · Export'),
]

box_w = 10.0
box_h = 1.35
start_x = 2.0
start_y = 17.8
gap = 1.62

for i, (num, title, subtitle) in enumerate(steps):
    y = start_y - i * gap
    box_x = start_x
    box_y = y - box_h / 2

    # Shadow
    shadow = FancyBboxPatch((box_x + 0.06, box_y - 0.06), box_w, box_h,
                             boxstyle='round,pad=0.08',
                             linewidth=0, facecolor='#AAAAAA', alpha=0.25,
                             zorder=1)
    ax.add_patch(shadow)

    # Gradient-like effect: main box
    grad_colors = [COLOR_BOX, COLOR_BOX_LIGHT]
    gc = grad_colors[i % 2]
    box = FancyBboxPatch((box_x, box_y), box_w, box_h,
                          boxstyle='round,pad=0.08',
                          linewidth=1.5, edgecolor=COLOR_BORDER,
                          facecolor=gc, zorder=2)
    ax.add_patch(box)

    # Step number circle
    circle = plt.Circle((box_x + 0.65, y), 0.38, color='#1B5E20', zorder=3)
    ax.add_patch(circle)
    circle_border = plt.Circle((box_x + 0.65, y), 0.38, color='#A5D6A7',
                                fill=False, linewidth=2, zorder=4)
    ax.add_patch(circle_border)
    ax.text(box_x + 0.65, y, num,
            fontsize=10, fontweight='bold', color='#A5D6A7',
            ha='center', va='center', zorder=5, fontfamily='Arial')

    # Title text
    ax.text(box_x + 1.35, y + 0.16, title,
            fontsize=13, fontweight='bold', color=COLOR_TEXT,
            ha='left', va='center', zorder=5, fontfamily='Arial')

    # Subtitle text
    ax.text(box_x + 1.35, y - 0.25, subtitle,
            fontsize=9, color='#C8E6C9',
            ha='left', va='center', zorder=5, fontfamily='Arial')

    # Arrow to next step
    if i < len(steps) - 1:
        arrow_y_start = box_y - 0.02
        arrow_y_end = box_y - (gap - box_h) + 0.04
        ax.annotate('', xy=(7, arrow_y_end), xytext=(7, arrow_y_start),
                    arrowprops=dict(arrowstyle='->', color=COLOR_ARROW,
                                   lw=2.5, mutation_scale=18),
                    zorder=6)

# Footer
ax.plot([1.0, 13.0], [0.55, 0.55], color='#4CAF50', linewidth=1)
ax.text(7, 0.28, 'Professional Tent Manufacturing | Quality at Every Step',
        fontsize=9, color='#4CAF50', ha='center', va='center',
        fontfamily='Arial', style='italic')

plt.tight_layout(pad=0.5)
output_path = r'C:\Users\Ray\.accio\accounts\1749967330\agents\DID-F456DA-2B0D4C\project\tent_manufacturing_flow.png'
plt.savefig(output_path, dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
print(f"Saved to {output_path}")
