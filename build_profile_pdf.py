# -*- coding: utf-8 -*-
"""Build the English-only Company & Manufacturing Profile PDF for Wanderfalke."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "Xinqiu-Company-Profile-Wanderfalke-2026-08.pdf")

BLACK = colors.HexColor("#111111")
GREY = colors.HexColor("#555555")
LINE = colors.HexColor("#999999")
LIGHT = colors.HexColor("#F2F2F2")

S = {}
S['title'] = ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=17,
                            leading=21, textColor=BLACK, spaceAfter=3)
S['sub'] = ParagraphStyle('sub', fontName='Helvetica', fontSize=10.5,
                          leading=14, textColor=BLACK, spaceAfter=1)
S['meta'] = ParagraphStyle('meta', fontName='Helvetica-Oblique', fontSize=9,
                           leading=12, textColor=GREY, spaceAfter=1)
S['h2'] = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11.5,
                         leading=15, textColor=BLACK, spaceBefore=13, spaceAfter=5)
S['body'] = ParagraphStyle('body', fontName='Helvetica', fontSize=9.7,
                           leading=14, textColor=BLACK, alignment=TA_JUSTIFY,
                           spaceAfter=6)
S['lead'] = ParagraphStyle('lead', fontName='Helvetica-Bold', fontSize=9.7,
                           leading=14, textColor=BLACK, spaceAfter=4)
S['bullet'] = ParagraphStyle('bullet', fontName='Helvetica', fontSize=9.7,
                             leading=13.6, textColor=BLACK, alignment=TA_LEFT,
                             leftIndent=11, bulletIndent=1, spaceAfter=4)
S['num'] = ParagraphStyle('num', fontName='Helvetica', fontSize=9.7,
                          leading=13.6, textColor=BLACK, alignment=TA_JUSTIFY,
                          leftIndent=14, bulletIndent=1, spaceAfter=5)
S['cell'] = ParagraphStyle('cell', fontName='Helvetica', fontSize=9.5,
                           leading=13, textColor=BLACK)
S['cellb'] = ParagraphStyle('cellb', fontName='Helvetica-Bold', fontSize=9.5,
                            leading=13, textColor=BLACK)
S['sign'] = ParagraphStyle('sign', fontName='Helvetica', fontSize=9.7,
                           leading=13.5, textColor=BLACK, spaceAfter=0)

B = lambda t: f"<b>{t}</b>"


def rule(space_before=6, space_after=4):
    t = Table([[""]], colWidths=[165 * mm], rowHeights=[0.1])
    t.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, 0), 0.5, LINE),
                           ("TOPPADDING", (0, 0), (-1, -1), 0),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return [Spacer(1, space_before), t, Spacer(1, space_after)]


def mktable(rows, widths, header=False):
    data = []
    for r_i, r in enumerate(rows):
        row = []
        for c in r:
            st = S['cellb'] if (header and r_i == 0) else S['cell']
            row.append(Paragraph(c, st))
        data.append(row)
    t = Table(data, colWidths=widths, hAlign='LEFT')
    style = [
        ("GRID", (0, 0), (-1, -1), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ]
    if header:
        style.append(("BACKGROUND", (0, 0), (-1, 0), LIGHT))
    t.setStyle(TableStyle(style))
    return t


story = []
A = story.append

# ---------------- Header block ----------------
A(Paragraph("Company &amp; Manufacturing Profile", S['title']))
A(Paragraph(B("Ningbo Xinqiu Tourism Products Co., Ltd."), S['sub']))
A(Spacer(1, 3))
A(Paragraph("Prepared for: Wanderfalke UG &amp; Co. KG &mdash; TUNNEL Tent Programme 2027",
            S['meta']))
story.extend(rule(7, 8))

# ---------------- Opening ----------------
A(Paragraph("Dear Andrej,", S['body']))
A(Paragraph(
    "Thank you for the clear questions. Below is a direct answer to each of them. "
    "Every figure here is our actual operating number, and where our structure needs "
    "explaining rather than a single number, we explain it &mdash; including one point "
    "about our BSCI report that we would rather raise ourselves than have you discover "
    "later.", S['body']))

# ---------------- Company basics ----------------
A(Paragraph("Company basics", S['h2']))
for k, v in [
    ("Company:", "Ningbo Xinqiu Tourism Products Co., Ltd."),
    ("Brands:", "XINQIU TENT / wind valley &mdash; www.xinqiutent.com"),
    ("Established:", "2006 &mdash; 20 years in tent manufacturing, OEM/ODM only"),
    ("Headquarters &amp; own plant:",
     "Ningbo, Zhejiang, China &mdash; approx. 30 minutes from the port"),
    ("Social compliance:", "BSCI audited (scope: Ningbo own plant &mdash; see section 1)"),
]:
    A(Paragraph(f"{B(k)} {v}", S['bullet'], bulletText="\u2013"))

# ---------------- 1 ----------------
A(Paragraph("1.  Team size &mdash; factory and administration", S['h2']))
A(Paragraph("Our manufacturing runs on two sites, and we want to be precise about "
            "which people sit where.", S['body']))
A(Paragraph(B("Ningbo &mdash; our own plant (covered by our BSCI report): 36 people"),
            S['lead']))
A(mktable([["Function", "Headcount"],
           ["Production line staff", "24"],
           ["Management", "4"],
           ["Sales &amp; merchandising", "3"],
           ["Design", "1"],
           ["Technical / pattern making", "2"],
           [B("Total"), B("36")]],
          [95 * mm, 30 * mm], header=True))
A(Spacer(1, 9))
A(Paragraph(B("Anhui &mdash; two partner factories: approx. 200 sewing operators"),
            S['lead']))
A(Paragraph(
    "These two factories are not owned by us and we hold no equity in them. The "
    "relationship is structural rather than casual: " +
    B("we supply the production equipment, and in return our orders take scheduling "
      "priority on those lines.") +
    " They are not ad-hoc subcontractors we shop around for each season.", S['body']))
A(Paragraph(
    B("Please note: our BSCI report covers the Ningbo own plant only.") +
    " The Anhui partner factories are not within its scope. We are telling you this "
    "upfront because you will otherwise compare 36 employees against our stated annual "
    "output and reasonably conclude the numbers do not add up. They do &mdash; the "
    "volume sits in Anhui.", S['body']))

# ---------------- 2 ----------------
A(KeepTogether([
    Paragraph("2.  Annual production capacity for tents", S['h2']),
    mktable([["Annual tent output", "approx. " + B("200,000 units")],
             ["Peak monthly shipment", "up to " + B("20,000 units")],
             ["Production lines",
              B("1") + " in Ningbo + " + B("15") + " in Anhui = " + B("16 total")],
             ["Industrial sewing machines", "approx. " + B("300 units")]],
            [62 * mm, 88 * mm]),
]))
A(Spacer(1, 9))
A(Paragraph(
    "The single Ningbo line is deliberate, not a limitation. It runs sampling, small "
    "runs and high-end custom work, where speed of iteration matters more than volume. "
    "The 15 Anhui lines carry mass production. For your TUNNEL programme this means "
    "development rounds stay fast at head office, and the production order is "
    "delivered at scale.", S['body']))

# ---------------- 3 ----------------
A(Paragraph("3.  Size of the production facilities", S['h2']))
A(Paragraph(B("Ningbo headquarters &mdash; 3,300 m&sup2;") +
            ", moved into this new site in 2026. Positioned as our sampling, showroom "
            "and high-end customisation base.", S['bullet'], bulletText="\u2013"))
A(Paragraph(B("Anhui partner factories &mdash; 15,000 m&sup2;") +
            ", the volume production base.", S['bullet'], bulletText="\u2013"))

# ---------------- 4 ----------------
A(Paragraph("4.  European and international brands we manufacture for", S['h2']))
A(Paragraph("We work exclusively as an OEM/ODM manufacturer. We do not sell a competing "
            "retail brand into our customers' markets.", S['body']))
A(Paragraph("Rather than a list of names, here is where our output actually goes:",
            S['body']))
A(mktable([["Destination", "Share of exports"],
           ["United States", "30%"],
           ["Spain", "20%"],
           ["Austria", "15%"],
           ["Other EU countries", "35%"]],
          [95 * mm, 33 * mm], header=True))
A(Spacer(1, 9))
A(Paragraph("That means roughly " + B("70% of our output ships into Europe") +
            " &mdash; EU packaging requirements, EU-market retail expectations and "
            "European seasonal timing are routine for us, not a learning curve.",
            S['body']))

# ---------------- 5 ----------------
A(Paragraph("5.  Named references &mdash; and what we can offer instead", S['h2']))
A(Paragraph(
    "Our customer relationships are covered by non-disclosure agreements, so we are not "
    "in a position to name them. We would rather keep those agreements than impress you "
    "with a name list &mdash; you would expect the same protection for Wanderfalke, and "
    "you will have it.", S['body']))
A(Paragraph("What we can put in front of you instead:", S['body']))
for t in [
    B("Verified third-party audits:") + " our " + B("BSCI report") + " (Ningbo plant) "
    "and our " + B("SGS factory audit report") + " conducted through Alibaba.com. "
    "Both can be sent to you directly.",
    B("In-house testing:") + " a " + B("hydrostatic head tester") + " and a " +
    B("dedicated tent waterproof test chamber") + ", where a pitched tent is tested "
    "under simulated rainfall. We can test your TUNNEL sample in front of you on a "
    "live video call.",
    B("Lead times we commit to:") + " sampling " + B("7&ndash;15 days") +
    "; mass production " + B("approx. 45 days") + ", varying with peak and off-peak "
    "season.",
    B("Comparable work, shown physically:") + " during a factory visit or video "
    "walk-through we can show tunnel-construction tents currently on the line &mdash; "
    "seam taping, pole sleeve stitching, pitched inspection &mdash; without disclosing "
    "whose they are.",
]:
    A(Paragraph(t, S['bullet'], bulletText="\u2013"))

# ---------------- 6 ----------------
sec6_head = [
    Paragraph("6.  Photos and video of the production facilities &mdash; our proposal",
              S['h2']),
    Paragraph("We would rather show you the plants live than send a folder of selected "
              "photos.", S['body']),
]
items = [
    B("Live video walk-through &mdash; both sites.") + " A scheduled call on WhatsApp "
    "or WeChat, walking the Ningbo plant and, separately, the " +
    B("Anhui production lines") + ". You pick the route and can ask us to stop "
    "anywhere. Since Anhui is where your volume would actually be built, we think you "
    "should see it rather than take our word for it. Suggested slots: " +
    B("08:00&ndash;10:00 CET") + ", which is mid-afternoon our time and works well for "
    "both sides.",
    B("Targeted footage on request.") + " Tell us which processes matter for your "
    "TUNNEL construction &mdash; seam sealing, pole sleeve stitching, pitched "
    "inspection, the waterproof test chamber &mdash; and we will film those stations "
    "specifically, not a generic promotional clip.",
    B("New facility footage.") + " An overview video and photo set of the Ningbo site "
    "we moved into in 2026, plus the Anhui production floor.",
    B("Visit in person.") + " You are welcome at any time. We are approx. " +
    B("3.5 hours by car from Shanghai Pudong Airport") + ", and about 30 minutes from "
    "the port.",
]
sec6_head.append(Paragraph(items[0], S['num'], bulletText="1."))
A(KeepTogether(sec6_head))
for i, t in enumerate(items[1:], 2):
    A(Paragraph(t, S['num'], bulletText=f"{i}."))

# ---------------- Closing ----------------
close = [Paragraph(
    "We understand you are evaluating a long-term manufacturing partner, not placing a "
    "one-off order. We are comfortable being evaluated on that basis. If anything above "
    "raises a further question &mdash; particularly on the Ningbo / Anhui structure "
    "&mdash; please ask it directly.", S['body']),
    Spacer(1, 5),
    Paragraph("Best regards,", S['sign']),
    Spacer(1, 9),
    Paragraph(B("Ray"), S['sign']),
    Paragraph("Ningbo Xinqiu Tourism Products Co., Ltd.", S['sign']),
    Paragraph("www.xinqiutent.com", S['sign'])]
A(Spacer(1, 6))
A(KeepTogether(close))


# ---------------- Page furniture ----------------
def decorate(canvas, doc):
    canvas.saveState()
    w, h = A4
    if doc.page > 1:
        canvas.setFont("Helvetica", 7.8)
        canvas.setFillColor(GREY)
        canvas.drawString(22 * mm, h - 13 * mm,
                          "Ningbo Xinqiu Tourism Products Co., Ltd.  |  "
                          "Company & Manufacturing Profile")
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.4)
        canvas.line(22 * mm, h - 15 * mm, w - 22 * mm, h - 15 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GREY)
    canvas.drawCentredString(w / 2.0, 12 * mm, f"Page {doc.page}")
    canvas.restoreState()


doc = BaseDocTemplate(OUT, pagesize=A4,
                      leftMargin=22 * mm, rightMargin=22 * mm,
                      topMargin=20 * mm, bottomMargin=20 * mm,
                      title="Company & Manufacturing Profile - "
                            "Ningbo Xinqiu Tourism Products Co., Ltd.",
                      author="Ningbo Xinqiu Tourism Products Co., Ltd.",
                      subject="Manufacturing capability profile for "
                              "Wanderfalke UG & Co. KG")
frame_first = Frame(22 * mm, 20 * mm, A4[0] - 44 * mm, A4[1] - 40 * mm, id='first')
frame_rest = Frame(22 * mm, 20 * mm, A4[0] - 44 * mm, A4[1] - 44 * mm, id='rest')
doc.addPageTemplates([
    PageTemplate(id='first', frames=[frame_first], onPage=decorate),
    PageTemplate(id='rest', frames=[frame_rest], onPage=decorate),
])
doc.build(story)
print("WROTE", OUT)
