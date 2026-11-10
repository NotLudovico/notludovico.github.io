"""Concept figure for the M.Sc. thesis card: firms interacting on a network + the relative LV model.

Run from the repo root:  python3 scripts/thesis_figure.py
Writes assets/img/thesis-concept.png. Needs matplotlib and a LaTeX install (usetex).
"""
import math
import random

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

FIRM = "#9aa3ad"

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    # upright symbols throughout (no italic variables); Agg paints each text one colour, so no xcolor
    "text.latex.preamble": r"\usepackage{amsmath}\usepackage[Euler]{upgreek}"
                           r"\newcommand{\x}{\mathrm{x}}\newcommand{\m}{\mathrm{m}}"
                           r"\newcommand{\h}{\vphantom{\frac{(\mathrm{W})}{\mathrm{m}}}}",
})

# (x, y, radius) in a 560 x 290 box, y pointing down like screen coords
NODES = [(48, 58, 10), (128, 36, 16), (214, 66, 9), (304, 40, 19), (392, 70, 11), (478, 44, 14),
         (526, 124, 8), (78, 148, 21), (178, 136, 12), (272, 158, 26), (374, 150, 10), (458, 168, 18),
         (40, 236, 8), (140, 228, 13), (238, 250, 9), (338, 238, 15), (432, 252, 7), (512, 232, 11)]

edges = [(a, b) for a in range(len(NODES)) for b in range(a + 1, len(NODES))
         if math.dist(NODES[a][:2], NODES[b][:2]) < 112]

# couplings as in the thesis, eq. (3.2): alpha = mu/C + sigma/sqrt(C) z, at the operating point
MU, SIGMA, C = -1.76, 1.75, 400
rng = random.Random(7)
alpha = {e: MU / C + SIGMA / math.sqrt(C) * rng.gauss(0, 1) for e in edges}
amax = max(abs(a) for a in alpha.values())
cmap = plt.get_cmap("RdBu")  # 0 = deep red (competitive), 1 = deep blue (cooperative)


def style(a):
    s = abs(a) / amax  # interaction strength in [0, 1]
    shade = 0.12 + 0.36 * s  # keep weak links visible, never white
    return cmap(0.5 - shade if a < 0 else 0.5 + shade), 0.9 + 2.0 * s


fig = plt.figure(figsize=(5.6, 4.1))
net = fig.add_axes([0.02, 0.33, 0.96, 0.65])
net.set_xlim(20, 545)
net.set_ylim(272, 18)  # flip y  # flip y
net.set_aspect("equal")
net.axis("off")

for (a, b), al in sorted(alpha.items(), key=lambda kv: abs(kv[1])):  # strong links on top
    (x1, y1, _), (x2, y2, _) = NODES[a], NODES[b]
    color, lw = style(al)
    net.plot([x1, x2], [y1, y2], color=color, lw=lw, solid_capstyle="round", zorder=1)

for x, y, r in NODES:
    net.add_patch(plt.Circle((x, y), r, color=FIRM, ec="white", lw=1.5, zorder=2))

eq = (r"$\dot{\x}_\mathrm{i} = \x_\mathrm{i}\Big(\underbrace{\h 1}_{\text{growth}}"
      r"\;\underbrace{\h -\,\frac{\x_\mathrm{i}}{\m}}_{\text{self-limitation}}"
      r"\;\underbrace{\h +\,\frac{(\mathrm{W}\x)_\mathrm{i}}{\m}}_{\text{interactions}}\Big)"
      r"\;+\;\underbrace{\h \uplambda\,(\m-\x_\mathrm{i})}_{\text{entry}}$")
fig.text(0.5, 0.235, eq, fontsize=19, ha="center", va="center", color="#20242a")

fig.savefig("assets/img/thesis-concept.png", dpi=220, facecolor="white", bbox_inches="tight", pad_inches=0.08)

n_coop = sum(a > 0 for a in alpha.values())
print(f"{n_coop}/{len(alpha)} links cooperative")
