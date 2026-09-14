#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds the static site into dist/.

    python3 build.py

Everything you would normally want to change lives in content.py.
"""

import html
import os
import re
import shutil
import sys

import content as C

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "dist")
SITE = C.SITE


def esc(s):
    return html.escape(s, quote=True)


def img_file(name, size):
    """Old-site photos are WebP; licensed replacements may arrive as JPEG."""
    for ext in (".webp", ".jpg", ".jpeg", ".png"):
        if os.path.isfile(os.path.join(ROOT, "assets", "img", size, name + ext)):
            return "/assets/img/%s/%s%s" % (size, name, ext)
    raise SystemExit("missing image: assets/img/%s/%s.*" % (size, name))


def img(name, cls="", alt="", size="full", **attrs):
    bits = " ".join('%s="%s"' % (k.replace("_", "-"), esc(str(v))) for k, v in attrs.items())
    return '<img src="%s" alt="%s"%s%s>' % (
        img_file(name, size), esc(alt),
        ' class="%s"' % cls if cls else "",
        " " + bits if bits else "",
    )


ICON_PHONE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
              'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9'
              'v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1'
              ' 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a'
              '16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>')

ICON_MAIL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4"'
             ' width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg>')


def maps_url():
    from urllib.parse import quote_plus
    return "https://www.google.com/maps/search/?api=1&query=" + quote_plus(
        ", ".join(SITE["address"]))


def directions_url():
    from urllib.parse import quote_plus
    return "https://www.google.com/maps/dir/?api=1&destination=" + quote_plus(
        ", ".join(SITE["address"]))


# --------------------------------------------------------------------------
# chrome


def head(lang, path, title, meta):
    ui = C.UI[lang]
    alt = C.ALTERNATES.get(path)
    full_title = "%s — %s" % (title, SITE["name"]) if path not in ("/", "/en/") else \
                 "%s — %s" % (SITE["name"], SITE["tagline_fr" if lang == "fr" else "tagline_en"])
    links = ""
    if alt:
        other = ui["lang_other_code"]
        links = ('<link rel="alternate" hreflang="%s" href="%s%s">'
                 '<link rel="alternate" hreflang="%s" href="%s%s">') % (
            lang, SITE["domain"], path, other, SITE["domain"], alt)
    return """<!doctype html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(meta)s">
<link rel="canonical" href="%(domain)s%(path)s">
%(links)s
<meta property="og:type" content="website">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(meta)s">
<meta property="og:url" content="%(domain)s%(path)s">
<meta property="og:image" content="%(domain)s/assets/img/full/%(hero)s.webp">
<meta property="og:locale" content="%(locale)s">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">%(skip)s</a>
""" % {
        "lang": lang, "title": esc(full_title), "meta": esc(meta), "domain": SITE["domain"],
        "path": path, "links": links, "hero": C.HERO, "skip": esc(ui["skip"]),
        "locale": "fr_FR" if lang == "fr" else "en_GB",
    }


def header(lang, path):
    ui = C.UI[lang]
    items = "".join(
        '<a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if href == path else "", esc(label))
        for href, label in C.NAV[lang]
    )
    alt = C.ALTERNATES.get(path, "/en/" if lang == "fr" else "/")
    home = "/" if lang == "fr" else "/en/"
    return """<header class="site-head">
<div class="wrap head-in">
<a class="brand" href="%(home)s">
<img src="/assets/favicon-32.png" alt="" width="26" height="26">
<span><b>Danse la Source</b><span class="sub">Trézelles · Allier</span></span>
</a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav">%(menu)s</button>
<nav class="nav" id="nav" aria-label="%(menu)s">%(items)s</nav>
<div class="head-tools">
<a class="lang" href="%(alt)s" hreflang="%(other)s"><span class="lang-full">%(langlabel)s</span><span class="lang-short">%(langshort)s</span></a>
<a class="btn btn-primary head-phone" href="tel:%(tel)s">%(icon)s%(phone)s</a>
</div>
</div>
</header>
""" % {
        "home": home, "menu": esc(ui["menu"]), "items": items, "alt": alt,
        "other": ui["lang_other_code"], "langlabel": esc(ui["lang_other"]),
        "langshort": esc(ui["lang_other_code"].upper()),
        "tel": SITE["phone_tel"], "phone": esc(SITE["phone_display"]), "icon": ICON_PHONE,
    }


def footer(lang):
    ui = C.UI[lang]
    booking = C.BOOKING_FR if lang == "fr" else C.BOOKING_EN
    return """<footer class="site-foot">
<div class="wrap">
<div class="foot-grid">
<div>
<h3>%(contact)s</h3>
<p><a href="tel:%(tel)s">%(phone)s</a></p>
<p><a href="mailto:%(email)s">%(email)s</a></p>
<p>%(hosts)s</p>
</div>
<div>
<h3>%(where)s</h3>
<p>%(addr)s</p>
<p><a href="%(map)s">%(maplink)s</a></p>
</div>
<div>
<h3>%(book)s</h3>
<p>%(booktext)s</p>
<p><a class="btn btn-ghost" href="%(booking)s">Gîtes de France</a></p>
</div>
</div>
<div class="foot-bot">
<span>© %(year)s %(name)s · %(rights)s</span>
<span><a href="%(alt)s">%(langlabel)s</a></span>
</div>
</div>
</footer>
<script src="/assets/js/gallery.js" defer></script>
</body>
</html>
""" % {
        "contact": esc(ui["footer_contact"]), "tel": SITE["phone_tel"],
        "phone": esc(SITE["phone_display"]), "email": esc(SITE["email"]),
        "hosts": esc(SITE["hosts"]), "where": esc(ui["footer_where"]),
        "addr": "<br>".join(esc(a) for a in SITE["address"]),
        "map": maps_url(), "maplink": esc(C.HOME[lang]["map_link"]),
        "dir": directions_url(), "dirlink": esc(ui["directions"]),
        "book": esc(ui["footer_book"]), "booktext": esc(ui["footer_book_text"]),
        "booking": booking, "year": 2026, "name": esc(SITE["name"]),
        "rights": esc(ui["rights"]),
        "alt": "/en/" if lang == "fr" else "/", "langlabel": esc(ui["lang_other"]),
    }


def lightbox(lang):
    ui = C.UI[lang]
    return """<div class="lb" id="lightbox" hidden role="dialog" aria-modal="true" aria-label="%(alt)s">
<div class="lb-bar">
<span class="lb-count"></span>
<button class="lb-close" type="button" aria-label="%(close)s">&#10005;</button>
</div>
<div class="lb-img"><img src="" alt=""></div>
<div class="lb-bar">
<button class="lb-prev" type="button" aria-label="%(prev)s">&#8249;</button>
<p class="lb-cap"></p>
<button class="lb-next" type="button" aria-label="%(next)s">&#8250;</button>
</div>
</div>
""" % {"close": esc(ui["close"]), "prev": esc(ui["prev"]), "next": esc(ui["next"]),
       "alt": esc(ui["menu"])}


def gallery(shots, lang, modifier=""):
    cells = []
    for name, cap_fr, cap_en in shots:
        cap = cap_fr if lang == "fr" else cap_en
        cells.append(
            '<figure><button type="button" data-shot="%s" data-alt="%s">'
            '%s<figcaption>%s</figcaption></button></figure>' % (
                img_file(name, "full"), esc(cap),
                img(name, size="thumb", alt=cap, loading="lazy", decoding="async",
                    width=600, height=450),
                esc(cap))
        )
    return '<div class="gallery%s">%s</div>' % (
        " " + modifier if modifier else "", "".join(cells))


# --------------------------------------------------------------------------
# pages


def page_home(lang):
    d = C.HOME[lang]
    path = "/" if lang == "fr" else "/en/"
    facts = "".join("<div><b>%s</b><span>%s</span></div>" % (esc(a), esc(b)) for a, b in d["facts"])
    body = "".join("<p>%s</p>" % b for b in d["body"])
    booking = C.BOOKING_FR if lang == "fr" else C.BOOKING_EN
    ui = C.UI[lang]
    return head(lang, path, d["title"], d["meta"]) + header(lang, path) + """
<main id="main">
<section class="hero">
<div class="hero-media">
%(hero)s
<div class="wrap hero-in">
<p class="eyebrow">%(tagline)s</p>
<h1>%(h1)s</h1>
<p>%(lede)s</p>
<div class="hero-actions">
<a class="btn btn-primary" href="%(cta_href)s">%(cta)s</a>
<a class="btn btn-ghost" href="%(booking)s">Gîtes de France</a>
</div>
</div>
</div>
</section>

<section class="section">
<div class="wrap split">
<div class="prose">%(body)s</div>
<aside>
<div class="card">
<h3>%(facts_title)s</h3>
<div class="facts" style="margin-top:1rem">%(facts)s</div>
</div>
</aside>
</div>
</section>

<section class="section">
<div class="wrap">
<div class="callout">
<h2>%(access_title)s</h2>
<p>%(access)s</p>
<p>%(addr)s</p>
<a class="btn btn-ghost" href="%(dir)s">%(dirlink)s</a>
</div>
</div>
</section>

<section class="section">
<div class="wrap">
%(gallery)s
</div>
</section>
%(lb)s
</main>
""" % {
        "hero": img(C.HERO, alt="", fetchpriority="high", decoding="async"),
        "tagline": esc(SITE["tagline_fr" if lang == "fr" else "tagline_en"]),
        "h1": d["h1"], "lede": d["lede"], "cta": esc(d["cta"]), "cta_href": d["cta_href"],
        "booking": booking, "body": body, "facts_title": esc(d["facts_title"]), "facts": facts,
        "access_title": esc(d["access_title"]), "access": esc(d["access"]),
        "addr": ", ".join(esc(a) for a in SITE["address"]),
        "dir": directions_url(), "dirlink": esc(ui["directions"]),
        "gallery": gallery(C.GALLERY_HOUSE[:8], lang), "lb": lightbox(lang),
    } + footer(lang)


def page_cottage(lang):
    d = C.COTTAGE[lang]
    path = "/fr/le-gite" if lang == "fr" else "/en/cottage"
    booking = C.BOOKING_FR if lang == "fr" else C.BOOKING_EN

    specs = ""
    for label, subs in d["specs"]:
        sub = "<ul>%s</ul>" % "".join("<li>%s</li>" % esc(s) for s in subs) if subs else ""
        specs += "<li>%s%s</li>" % (esc(label), sub)

    comfort = "".join("<li>%s</li>" % esc(c) for c in d["comfort"])
    studio_specs = "".join("<li>%s</li>" % esc(s) for s in d["studio_specs"])
    book = d["book"].format(booking=booking, tel=SITE["phone_tel"], phone=SITE["phone_display"])

    return head(lang, path, d["title"], d["meta"]) + header(lang, path) + """
<main id="main">
<section class="wrap page-head">
<p class="eyebrow">Danse la Source</p>
<h1>%(h1)s</h1>
<p class="lede">%(lede)s</p>
</section>

<section class="section">
<div class="wrap split">
<div>
<h2>%(spec_title)s</h2>
<ul class="specs" style="margin-top:1.2rem">%(specs)s</ul>
</div>
<aside>
<div class="card">
<h3>%(comfort_title)s</h3>
<ul class="chips" style="margin-top:.9rem">%(comfort)s</ul>
</div>
</aside>
</div>
</section>

<section class="section">
<div class="wrap">
<h2>%(garden_title)s</h2>
<p class="lede">%(garden)s</p>
</div>
</section>

<section class="section">
<div class="wrap">
<h2>%(gallery_title)s</h2>
<div style="margin-top:1.5rem">%(gallery)s</div>
</div>
</section>

<section class="section" id="studio">
<div class="wrap">
<h2>%(studio_h)s</h2>
<div class="section-narrow">
<p class="lede">%(studio_body)s</p>
<ul class="specs" style="margin-top:1.2rem">%(studio_specs)s</ul>
</div>
<div style="margin-top:2rem">%(studio_gallery)s</div>
</div>
</section>

<section class="section">
<div class="wrap">
<div class="callout">
<h2>%(book_title)s</h2>
<p>%(book)s</p>
<a class="btn btn-ghost" href="tel:%(tel)s">%(icon)s%(phone)s</a>
</div>
</div>
</section>
%(lb)s
</main>
""" % {
        "h1": esc(d["h1"]), "lede": esc(d["lede"]),
        "spec_title": esc(d["spec_title"]), "specs": specs,
        "comfort_title": esc(d["comfort_title"]), "comfort": comfort,
        "garden_title": esc(d["garden_title"]), "garden": esc(d["garden"]),
        "gallery_title": esc(d["gallery_title"]),
        "gallery": gallery(C.GALLERY_HOUSE, lang),
        "studio_h": esc(d["studio_h"]), "studio_body": esc(d["studio_body"]),
        "studio_specs": studio_specs,
        "studio_gallery": gallery(C.GALLERY_STUDIO, lang, "gallery--three"),
        "book_title": esc(d["book_title"]), "book": book,
        "tel": SITE["phone_tel"], "phone": esc(SITE["phone_display"]), "icon": ICON_PHONE,
        "lb": lightbox(lang),
    } + footer(lang)


def credits_block(names, lang):
    """CC BY-SA and friends require a visible credit wherever the photo is used."""
    items = []
    for n in names:
        c = C.PHOTO_CREDITS.get(n)
        if not c:
            continue
        items.append(
            '<li><a href="%s">%s</a> — <a href="%s">%s</a>, '
            '<a href="%s">%s</a> (%s)</li>' % (
                c["source"], esc(c["title"]), c["author_url"], esc(c["author"]),
                c["licence_url"], esc(c["licence"]), esc(c["changed"][lang])))
    if not items:
        return ""
    return ('<section class="section"><div class="wrap"><p class="credits-h">%s</p>'
            '<ul class="credits">%s</ul></div></section>' % (
                esc(C.CREDITS_LABEL[lang]), "".join(items)))


def page_attractions(lang):
    d = C.ATTRACTIONS_INTRO[lang]
    path = "/fr/loisirs" if lang == "fr" else "/en/nearby-attractions"
    cards = []
    for name, when, fr, en in C.ATTRACTIONS:
        label, url, text = fr if lang == "fr" else en
        cards.append("""<article class="thing">
%s
<div class="thing-body">
<span class="time">%s</span>
<h2><a href="%s">%s</a></h2>
<p>%s</p>
</div>
                  </article>""" % (img(name, size="full", alt=re.sub("<[^>]+>", "", label),
                      loading="lazy", decoding="async", width=800, height=500),
                  esc(when), url, label, text))

    return head(lang, path, d["title"], d["meta"]) + header(lang, path) + """
<main id="main">
<section class="wrap page-head">
<p class="eyebrow">Allier · Auvergne</p>
<h1>%(h1)s</h1>
<p class="lede">%(lede)s</p>
</section>
<section class="section">
<div class="wrap">
<div class="things">%(cards)s</div>
</div>
</section>
%(credits)s
</main>
""" % {"h1": esc(d["h1"]), "lede": d["lede"], "cards": "".join(cards),
       "credits": credits_block([a[0] for a in C.ATTRACTIONS], lang)} + footer(lang)


def page_redirect(src, dst):
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=%(dst)s">
<link rel="canonical" href="%(domain)s%(dst)s">
<meta name="robots" content="noindex">
<title>Danse la Source</title>
</head>
<body>
<p>Cette page a déménagé. <a href="%(dst)s">Continuer &rarr;</a></p>
<script>location.replace("%(dst)s");</script>
</body>
</html>
""" % {"dst": dst, "domain": SITE["domain"]}


def page_404():
    return head("fr", "/404", "Page introuvable",
                "Cette page n'existe pas.") + header("fr", "/") + """
<main id="main">
<section class="wrap page-head" style="min-height:48svh">
<p class="eyebrow">Erreur 404</p>
<h1>Page introuvable</h1>
<p class="lede">Cette page n'existe pas ou a déménagé.<br>
<span lang="en">This page does not exist or has moved.</span></p>
<p style="margin-top:1.5rem">
<a class="btn btn-primary" href="/">Retour à l'accueil</a>
<a class="btn btn-ghost" href="/en/" style="margin-left:.5rem">English</a>
</p>
</section>
</main>
""" + footer("fr")


# --------------------------------------------------------------------------


def jsonld():
    return """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"VacationRental",
"name":"%(name)s",
"description":"%(desc)s",
"url":"%(domain)s/",
"telephone":"%(tel)s",
"email":"%(email)s",
"image":"%(domain)s/assets/img/full/%(hero)s.webp",
"address":{"@type":"PostalAddress","streetAddress":"230 Rte de Floret","addressLocality":"Trézelles",
"postalCode":"03220","addressCountry":"FR"},
"geo":{"@type":"GeoCoordinates","latitude":%(lat)s,"longitude":%(lng)s},
"petsAllowed":true,
"numberOfRooms":6}
</script>"""  % {
        "name": SITE["name"], "desc": C.HOME["fr"]["meta"], "domain": SITE["domain"],
        "tel": SITE["phone_tel"], "email": SITE["email"], "hero": C.HERO,
        "lat": SITE["lat"], "lng": SITE["lng"],
    }


def write(path, text):
    target = os.path.join(OUT, path.lstrip("/"))
    if path.endswith("/"):
        target = os.path.join(target, "index.html")
    elif not target.endswith(".html"):
        target = os.path.join(target, "index.html")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(text)
    return target


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    pages = {
        "/": page_home("fr"),
        "/en/": page_home("en"),
        "/fr/le-gite": page_cottage("fr"),
        "/en/cottage": page_cottage("en"),
        "/fr/loisirs": page_attractions("fr"),
        "/en/nearby-attractions": page_attractions("en"),
    }
    # Structured data, on the French home page only.
    pages["/"] = pages["/"].replace("</head>", jsonld() + "\n</head>")

    written = []
    for path, text in pages.items():
        written.append(write(path, text))

    for src, dst in C.REDIRECTS.items():
        written.append(write(src, page_redirect(src, dst)))

    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as fh:
        fh.write(page_404())

    # sitemap + robots
    urls = "".join(
        "<url><loc>%s%s</loc><changefreq>yearly</changefreq></url>" % (SITE["domain"], p)
        for p in pages
    )
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>\n' % urls)
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE["domain"])

    # Cloudflare Pages / Netlify honour these; harmless elsewhere.
    with open(os.path.join(OUT, "_redirects"), "w", encoding="utf-8") as fh:
        for src, dst in C.REDIRECTS.items():
            fh.write("%s %s 301\n" % (src, dst))

    # GitHub Pages reads the custom domain from this file; ignored elsewhere.
    with open(os.path.join(OUT, "CNAME"), "w", encoding="utf-8") as fh:
        fh.write(SITE["domain"].split("://")[1] + "\n")

    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"))

    total = sum(
        os.path.getsize(os.path.join(dp, f))
        for dp, _, fs in os.walk(OUT) for f in fs
    )
    print("Built %d pages + %d redirects into dist/ (%.1f MB)" % (
        len(pages), len(C.REDIRECTS), total / 1e6))
    for w in sorted(written):
        print("  " + os.path.relpath(w, ROOT))


if __name__ == "__main__":
    sys.exit(main())
