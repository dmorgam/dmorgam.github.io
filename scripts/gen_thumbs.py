from PIL import Image, ImageDraw, ImageFont

W, H = 960, 540
BG = (30, 32, 48)
BORDER = (54, 58, 79)
AMBER = (183, 189, 248)
TEXT = (202, 211, 245)
MUTED = (165, 173, 203)

FONT_DIR = "/usr/share/fonts/TTF/"
BOLD = FONT_DIR + "JetBrainsMonoNerdFontMono-Bold.ttf"
REG = FONT_DIR + "JetBrainsMonoNerdFontMono-Regular.ttf"

# (filename, [(line, color, bold)])
cards = {
    "aiops_platform.png": [
        ("## plataforma agéntica aiops", AMBER, True),
        ("", TEXT, False),
        (" chat ────▶ ┌─────────┐    ┌─────────┐", TEXT, False),
        ("            │ agentes │──▶ │ mcp hub │", TEXT, False),
        (" eventos ─▶ └─────────┘    └────┬────┘", TEXT, False),
        ("                 │              │", TEXT, False),
        ("             guardrails      tools de", TEXT, False),
        ("             + policy        dominio", TEXT, False),
        ("", TEXT, False),
        (" microservicios · kubernetes · azure", MUTED, False),
    ],
    "agents.png": [
        ("## agentes con guardrails", AMBER, True),
        ("", TEXT, False),
        (" $ run --dry-run --required-tool mail", MUTED, False),
        ("", TEXT, False),
        (" think ──▶ act(tool) ──▶ observe", TEXT, False),
        ("   ▲                        │", TEXT, False),
        ("   └────────────────────────┘", TEXT, False),
        ("", TEXT, False),
        (" allow/deny · timeouts · auditoría", TEXT, False),
        (" langgraph · azure openai · mcp", MUTED, False),
    ],
    "policy.png": [
        ("## policy enforcement", AMBER, True),
        ("", TEXT, False),
        (" tool_call ──▶ ┌───────────────┐", TEXT, False),
        ("               │  rbac / abac  │", TEXT, False),
        ("               └───────┬───────┘", TEXT, False),
        ("                permit │", TEXT, False),
        ("               ┌───────▼───────┐", TEXT, False),
        ("               │   llm judge   │", TEXT, False),
        ("               └───────────────┘", TEXT, False),
        ("", TEXT, False),
        (" fail-closed · monotonic-deny", MUTED, False),
    ],
}

for name, lines in cards.items():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle([8, 8, W - 9, H - 9], outline=BORDER, width=2)

    title_f = ImageFont.truetype(BOLD, 38)
    body_f = ImageFont.truetype(REG, 30)
    body_b = ImageFont.truetype(BOLD, 30)

    n = len(lines)
    lh = 42
    total = 56 + (n - 1) * lh
    y = (H - total) // 2
    for i, (line, color, bold) in enumerate(lines):
        if i == 0:
            d.text((56, y), line, font=title_f, fill=color)
            y += 56
        else:
            d.text((56, y), line, font=(body_b if bold else body_f), fill=color)
            y += lh

    out = "/home/dmorgam/Git/dmorgam.github.io/main/public/img/" + name
    im.save(out)
    print(out)
