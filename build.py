"""Build index.html, llms.txt and sitemap.xml from site.py. Run: python3 build.py"""

import html
import json
from pathlib import Path

from brands import JOB, NAME, OPEN_SOURCE, PAGES_REPOS, SAME_AS, SECTIONS, SITE, UPDATED

ROOT = Path(__file__).parent
ME = f"{SITE}/#bez"
GSC_META = "yUmJsdzFlyhr7mQyyK-nCaXVORLxQtFbQYRZSFjVW-M"

TITLE = "Bez: AI systems architect and founder of 20 UK online businesses"
DESC = (
    "Bez builds and runs UK online businesses that Google ranks and AI assistants recommend: "
    "gift, pet, crystal and eSIM shops, a free car check, comparison sites, discount and referral codes, "
    "AI app development, online personal training and AI news."
)

e = html.escape
businesses = [b for _, _, _, items in SECTIONS for b in items]
COUNT = len(businesses)
SHOPS = len(SECTIONS[0][3])


def repo_url(repo: str) -> str:
    return f"{SITE}/{repo}/" if repo in PAGES_REPOS else f"https://github.com/behoss/{repo}"


def icon(file: str, name: str) -> str:
    return f'<img src="/img/{file}" alt="{e(name)} logo" width="48" height="48" decoding="async">'


def card(b) -> str:
    name, url, tag, ico, desc, cta = b
    return f"""      <article class="card">
        <div class="card-top">{icon(ico, name)}<span class="tag">{e(tag)}</span></div>
        <h3>{e(name)}</h3>
        <p>{e(desc)}</p>
        <a class="go" href="{url}">{e(cta)} <span aria-hidden="true">→</span></a>
        <span class="host">{e(url.removeprefix("https://"))}</span>
      </article>"""


def oss_card(r) -> str:
    repo, lang, desc, biz, biz_url = r
    return f"""      <article class="card oss">
        <div class="card-top"><span class="mono">behoss/</span><span class="tag">{e(lang)}</span></div>
        <h3>{e(repo)}</h3>
        <p>{e(desc)}</p>
        <a class="go" href="{repo_url(repo)}">Use {e(repo)} <span aria-hidden="true">→</span></a>
        <span class="host">Powers <a class="inline" href="{biz_url}">{e(biz)}</a></span>
      </article>"""


def section(sid, heading, strap, items) -> str:
    cards = "\n".join(card(b) for b in items)
    return f"""  <section id="{sid}" aria-labelledby="{sid}-h">
    <div class="wrap">
      <header class="sec-head"><h2 id="{sid}-h">{e(heading)}</h2><p>{e(strap)}</p></header>
      <div class="grid">
{cards}
      </div>
    </div>
  </section>"""


def json_ld() -> str:
    orgs = []
    for name, url, tag, ico, desc, _ in businesses:
        orgs.append({
            "@type": "Organization",
            "@id": f"{url}/#organization",
            "name": name,
            "url": url,
            "description": desc,
            "logo": f"{SITE}/img/{ico}",
            "founder": {"@id": ME},
        })
    code = [{
        "@type": "SoftwareSourceCode",
        "name": repo,
        "codeRepository": f"https://github.com/behoss/{repo}",
        "url": repo_url(repo),
        "description": desc,
        "author": {"@id": ME},
    } for repo, _, desc, _, _ in OPEN_SOURCE]
    graph = [
        {"@type": "WebSite", "@id": f"{SITE}/#website", "url": f"{SITE}/", "name": NAME,
         "inLanguage": "en-GB", "publisher": {"@id": ME}},
        {"@type": "ProfilePage", "@id": f"{SITE}/#webpage", "url": f"{SITE}/", "name": TITLE,
         "description": DESC, "inLanguage": "en-GB", "isPartOf": {"@id": f"{SITE}/#website"},
         "mainEntity": {"@id": ME}, "dateModified": UPDATED},
        {"@type": "BreadcrumbList", "@id": f"{SITE}/#breadcrumb",
         "itemListElement": [{"@type": "ListItem", "position": 1, "name": NAME, "item": f"{SITE}/"}]},
        {"@type": "Person", "@id": ME, "name": NAME, "alternateName": "behoss", "jobTitle": JOB,
         "url": f"{SITE}/", "sameAs": SAME_AS,
         "knowsAbout": ["Artificial intelligence", "Large language models", "AI agents",
                        "Retrieval-augmented generation", "Search engine optimisation",
                        "Generative engine optimisation", "E-commerce", "Software architecture"],
         "worksFor": {"@id": "https://softgen.co.uk/#organization"}},
        {"@type": "ItemList", "@id": f"{SITE}/#businesses", "name": f"Businesses {NAME} runs",
         "numberOfItems": COUNT,
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": {"@id": f"{b[1]}/#organization"}}
                             for i, b in enumerate(businesses)]},
        *orgs,
        *code,
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)


CSS = """
:root{--bg:#fbfaf7;--surface:#fff;--ink:#0b1220;--muted:#4b5563;--line:#e8e4db;--accent:#3730a3;--accent-ink:#fff;--soft:#eef0ff;--radius:18px;--wrap:1200px}
*{box-sizing:border-box}
html{scroll-padding-top:84px;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}
img{display:block;max-width:100%}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 28px}
.skip{position:absolute;left:-9999px}.skip:focus{left:16px;top:12px;background:#fff;padding:8px 12px;border-radius:8px;z-index:9}
/* header */
.top{position:sticky;top:0;z-index:5;background:rgba(251,250,247,.92);backdrop-filter:saturate(1.4) blur(10px);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;gap:28px;height:68px}
.brand{font-weight:800;font-size:24px;letter-spacing:-.03em;text-decoration:none}
.brand b{color:var(--accent)}
.nav{display:flex;gap:22px;margin-left:auto;font-size:15px;font-weight:500}
.nav a{text-decoration:none;color:var(--muted)}
.nav a:hover{color:var(--ink)}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 20px;border-radius:999px;font-weight:650;font-size:16px;text-decoration:none;border:1.5px solid var(--ink)}
.btn.primary{background:var(--ink);color:#fff}
.btn.primary:hover{background:var(--accent);border-color:var(--accent)}
.btn.ghost:hover{background:var(--ink);color:#fff}
.top .btn{padding:9px 16px;font-size:14px}
/* hero */
.hero{padding:88px 0 72px;border-bottom:1px solid var(--line);background:radial-gradient(1200px 420px at 85% -10%,#e7e9ff 0,rgba(231,233,255,0) 70%),radial-gradient(900px 380px at 0% 0%,#fff3e6 0,rgba(255,243,230,0) 65%)}
.eyebrow{display:inline-block;font-size:14px;font-weight:650;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);background:var(--soft);padding:6px 12px;border-radius:999px;margin:0 0 22px}
.hero h1{font-size:clamp(38px,5.6vw,68px);line-height:1.04;letter-spacing:-.035em;margin:0 0 22px;max-width:14ch;font-weight:800}
.hero .lead{font-size:clamp(18px,2vw,21px);color:var(--muted);max-width:60ch;margin:0 0 32px}
.ctas{display:flex;flex-wrap:wrap;gap:12px;margin-bottom:48px}
.hero .wrap{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr);gap:48px;align-items:center}
.hero .stats{grid-column:1/-1}
.wall{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;padding:26px;background:rgba(255,255,255,.7);border:1px solid var(--line);border-radius:28px;box-shadow:0 30px 60px -30px rgba(55,48,163,.25)}
.wall span{aspect-ratio:1;display:grid;place-items:center;background:#fff;border:1px solid var(--line);border-radius:16px}
.wall img{width:56%;height:auto;border-radius:10px}
.stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:0;border:1px solid var(--line);border-radius:var(--radius);background:var(--surface);overflow:hidden}
.stats div{padding:22px 24px;border-left:1px solid var(--line)}
.stats div:first-child{border-left:0}
.stats strong{display:block;font-size:34px;letter-spacing:-.03em;line-height:1.1}
.stats span{color:var(--muted);font-size:15px}
/* sections */
section{padding:76px 0;border-bottom:1px solid var(--line)}
.sec-head{display:flex;align-items:baseline;justify-content:space-between;gap:24px;flex-wrap:wrap;margin-bottom:30px}
.sec-head h2{font-size:clamp(28px,3.2vw,40px);letter-spacing:-.03em;margin:0;line-height:1.1}
.sec-head p{margin:0;color:var(--muted);font-size:17px}
.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.card{position:relative;display:flex;flex-direction:column;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:26px 26px 22px;box-shadow:0 1px 2px rgba(11,18,32,.04)}
.card:hover{border-color:#c9c3b5;box-shadow:0 10px 30px -12px rgba(11,18,32,.18)}
.card-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;min-height:48px}
.card-top img{width:48px;height:48px;border-radius:12px;box-shadow:0 0 0 1px rgba(11,18,32,.06)}
.tag{font-size:13px;font-weight:600;color:var(--muted);background:#f3f1ec;padding:5px 11px;border-radius:999px}
.card h3{font-size:22px;letter-spacing:-.02em;margin:0 0 8px;line-height:1.2}
.card p{margin:0 0 20px;color:var(--muted);font-size:16px;flex:1}
.go{font-weight:650;color:var(--accent);text-decoration:none;font-size:16px}
.go::after{content:"";position:absolute;inset:0;border-radius:var(--radius)}
.card:hover .go{text-decoration:underline;text-underline-offset:3px}
.host{display:block;margin-top:6px;font-size:13px;color:#8a8f98}
.host .inline{position:relative;z-index:1;color:var(--ink);font-weight:600}
.mono{font:600 14px/1 ui-monospace,SFMono-Regular,Menlo,monospace;color:#8a8f98}
.oss h3{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:19px}
/* softgen band */
.band{background:var(--ink);color:#fff;border-radius:24px;padding:48px;display:flex;align-items:center;justify-content:space-between;gap:32px;flex-wrap:wrap}
.band h2{margin:0 0 8px;font-size:clamp(26px,3vw,36px);letter-spacing:-.03em;line-height:1.15}
.band p{margin:0;color:#c7cbe0;max-width:56ch}
.band .btn{background:#fff;color:var(--ink);border-color:#fff}
.band .btn:hover{background:var(--soft);border-color:var(--soft)}
.stack{margin-top:26px;color:var(--muted);font-size:15px}
/* footer */
footer{padding:40px 0 56px;color:var(--muted);font-size:15px}
footer .wrap{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}
footer nav{display:flex;gap:20px}
footer a{text-decoration:none}footer a:hover{color:var(--ink);text-decoration:underline}
:focus-visible{outline:3px solid var(--accent);outline-offset:3px;border-radius:6px}
@media (max-width:1020px){.hero .wrap{grid-template-columns:1fr}.wall{grid-template-columns:repeat(10,1fr);padding:14px;gap:8px;border-radius:20px}.wall span{border-radius:10px}.wall img{width:72%}.grid{grid-template-columns:repeat(2,minmax(0,1fr))}.nav{display:none}.top .btn{margin-left:auto}}
@media (max-width:640px){.wall{grid-template-columns:repeat(5,1fr)}.ctas{margin-bottom:28px}.wrap{padding:0 20px}.grid{grid-template-columns:1fr}.hero{padding:56px 0 48px}section{padding:56px 0}.stats{grid-template-columns:repeat(2,minmax(0,1fr))}.stats div:nth-child(3){border-left:0}.stats div:nth-child(n+3){border-top:1px solid var(--line)}.band{padding:32px 26px}.ctas .btn{flex:1;justify-content:center}}
"""


def page() -> str:
    sections = "\n".join(section(*s) for s in SECTIONS)
    oss = "\n".join(oss_card(r) for r in OPEN_SOURCE)
    wall = "".join(f'<span><img src="/img/{b[3]}" alt="" width="44" height="44"></span>' for b in businesses)
    nav = "".join(f'<a href="#{sid}">{e(h.split(" and ")[0])}</a>' for sid, h, _, _ in SECTIONS)
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(TITLE)}</title>
<meta name="description" content="{e(DESC)}">
<link rel="canonical" href="{SITE}/">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="google-site-verification" content="{GSC_META}">
<meta name="theme-color" content="#fbfaf7">
<meta name="color-scheme" content="light">
<meta property="og:type" content="profile">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{e(TITLE)}">
<meta property="og:description" content="{e(DESC)}">
<meta property="og:url" content="{SITE}/">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@bezhoss">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="text/plain" href="/llms.txt" title="llms.txt">
<style>{CSS.strip()}</style>
<script type="application/ld+json">
{json_ld()}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="wrap">
    <a class="brand" href="/" aria-label="{NAME}, home">Bez<b>.</b></a>
    <nav class="nav" aria-label="Sections">{nav}<a href="#open-source">Open source</a></nav>
    <a class="btn primary" href="https://softgen.co.uk">Build with Softgen</a>
  </div>
</header>
<main id="main">
  <div class="hero">
    <div class="wrap">
      <div class="hero-copy">
      <p class="eyebrow">{e(JOB)}</p>
      <h1>I build UK online businesses that Google ranks and AI recommends.</h1>
      <p class="lead">Shops, a free car check, comparison sites, codes and bonuses, AI services and AI news. Each one is built to be the clearest answer to what people search for, on Google and in ChatGPT, Gemini and Perplexity.</p>
      <div class="ctas"><a class="btn primary" href="#shops">See the businesses</a><a class="btn ghost" href="#open-source">Free tools and data</a></div>
      </div>
      <div class="wall" aria-hidden="true">{wall}</div>
      <div class="stats">
        <div><strong>{COUNT}</strong><span>UK businesses</span></div>
        <div><strong>{SHOPS}</strong><span>online shops</span></div>
        <div><strong>200+</strong><span>countries served by eSIM</span></div>
        <div><strong>10 yrs</strong><span>building software</span></div>
      </div>
    </div>
  </div>
{sections}
  <section id="open-source" aria-labelledby="open-source-h">
    <div class="wrap">
      <header class="sec-head"><h2 id="open-source-h">Open source</h2><p>Free tools and open data from the businesses above.</p></header>
      <div class="grid">
{oss}
      </div>
    </div>
  </section>
  <section aria-labelledby="build-h" style="border-bottom:0">
    <div class="wrap">
      <div class="band">
        <div>
          <h2 id="build-h">Want an AI product built like these?</h2>
          <p>Softgen designs and ships AI apps, SaaS platforms, MVPs and mobile apps, fixed price and live in weeks, built to rank on Google and get quoted by AI assistants.</p>
        </div>
        <a class="btn" href="https://softgen.co.uk/contact">Get a fixed-price quote <span aria-hidden="true">→</span></a>
      </div>
      <p class="stack">How I build: Python · TypeScript · Swift · Next.js · FastAPI · PostgreSQL · Neo4j · Cloudflare · AWS · Claude, GPT and Gemini · RAG, agents and tool calling · voice AI · SEO and GEO.</p>
    </div>
  </section>
</main>
<footer>
  <div class="wrap">
    <span>© 2026 {NAME}</span>
    <nav aria-label="Profiles"><a href="https://github.com/behoss" rel="me">GitHub</a><a href="https://x.com/bezhoss" rel="me">X</a><a href="https://www.linkedin.com/in/bhoss" rel="me">LinkedIn</a><a href="/llms.txt">llms.txt</a></nav>
  </div>
</footer>
</body>
</html>
"""


def llms() -> str:
    out = [f"# {NAME}", "", f"> {DESC}", "",
           f"{NAME} is an {JOB} who founded and runs the {COUNT} UK online businesses below.", ""]
    for _, heading, _, items in SECTIONS:
        out.append(f"## {heading}")
        out += [f"- [{n}]({u}): {d}" for n, u, _, _, d, _ in items]
        out.append("")
    out.append("## Open source")
    out += [f"- [{r}]({repo_url(r)}): {d} Powers {b} ({bu})." for r, _, d, b, bu in OPEN_SOURCE]
    out += ["", "## Profiles", *[f"- {u}" for u in SAME_AS], ""]
    return "\n".join(out)


def sitemap() -> str:
    urls = [f"{SITE}/"] + [f"{SITE}/{r}/" for r in sorted(PAGES_REPOS)]
    body = "".join(f"<url><loc>{u}</loc><lastmod>{UPDATED}</lastmod></url>" for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>\n'


if __name__ == "__main__":
    (ROOT / "index.html").write_text(page())
    (ROOT / "llms.txt").write_text(llms())
    (ROOT / "sitemap.xml").write_text(sitemap())
    print(f"built: {COUNT} businesses, {len(OPEN_SOURCE)} repos, {len(page())//1024} KB index.html")
