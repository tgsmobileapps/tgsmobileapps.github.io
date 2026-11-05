"""Builds index.html and terms/<app>.html from one app table.

    python3 _build/build.py

Jekyll ignores folders starting with "_", so this script is not published.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UPDATED = "November 5, 2026"
EMAIL = "tgsmobileapps@gmail.com"
OWNER = "Selçuk Gedikkaya, trading as TGS Mobile Apps"

APPS = [
    dict(
        slug="meditrack", name="MediTrack: AI Pill Tracker", icon="meditrack.jpg",
        tagline="Medicine, dose and fever tracking for your family, with AI that reads medicine boxes.",
        ios="https://apps.apple.com/app/id6761290878",
        play="https://play.google.com/store/apps/details?id=com.tgsmobileapps.meditrack",
        what="tracks medicines, doses, supplements and temperature readings, and uses AI to read medicine packaging",
        ai=True, account=False, medical=True,
        extra=[
            ("Dosing is your responsibility",
             "MediTrack shows the information you enter and reminders you set. It does not calculate or "
             "recommend doses. Always follow the package leaflet and the advice of your doctor or pharmacist. "
             "Reminders can be delayed or blocked by your device settings, so do not rely on them alone for "
             "time-critical medication."),
        ],
    ),
    dict(
        slug="shottime", name="GLP 1 Shot Tracker: ShotTime", icon="shottime.jpg",
        tagline="Log GLP-1 shots, doses, weight and nutrition, and see your progress at a glance.",
        ios=None, play=None,
        what="logs GLP-1 medication shots, doses, injection sites, weight and nutrition",
        ai=True, account=False, medical=True,
        extra=[
            ("Not a medical device",
             "ShotTime is a personal logbook. It does not prescribe, adjust or recommend doses and is not a "
             "medical device. Decisions about your medication belong to you and your healthcare provider."),
        ],
    ),
    dict(
        slug="objectrelay", name="ObjectRelay AI: Find My Things", icon="objectrelay.jpg",
        tagline="Snap a shelf or a drawer and AI lists every item, so you can find anything in seconds.",
        ios="https://apps.apple.com/app/id6762591217",
        play="https://play.google.com/store/apps/details?id=com.tgsmobileapps.object.relay",
        what="builds an inventory of your belongings from photos, lets you search it, track lent items and share spaces",
        ai=True, account=False, medical=False,
        extra=[
            ("Estimated values and expiry dates",
             "Resale values are rough AI estimates, not appraisals, and must not be used as the sole basis for "
             "insurance claims, sales or tax purposes. Expiry dates read from photos must be checked against the "
             "product label."),
            ("Shared spaces",
             "When you share a space with an invite code, everyone with the code can see and change its items. "
             "Share codes only with people you trust. You are responsible for what you add to shared spaces."),
        ],
    ),
    dict(
        slug="botanic", name="AI Plant Identifier - Botanic", icon="botanic.jpg",
        tagline="Identify plants, diagnose problems and get care reminders for your garden.",
        ios="https://apps.apple.com/app/id6779547023",
        play="https://play.google.com/store/apps/details?id=com.tgsmobileapps.botanic.ai.plant.identifier",
        what="identifies plants from photos, suggests care and sends watering reminders",
        ai=True, account=True, medical=False,
        extra=[
            ("Toxicity and edibility",
             "Never eat, use medicinally or let children or pets touch a plant based only on the app's result. "
             "Identification can be wrong, and some plants are dangerous. Ask an expert first."),
        ],
    ),
    dict(
        slug="authenticator", name="Authenticator App - MFA / 2FA", icon="authenticator.jpg",
        tagline="Two-factor codes for all your accounts, stored securely on your device.",
        ios="https://apps.apple.com/app/id6760597863",
        play="https://play.google.com/store/apps/details?id=com.tgsmobileapps.authenticator",
        what="generates two-factor authentication codes and stores your 2FA secrets on your device",
        ai=False, account=False, medical=False,
        extra=[
            ("Keep your own backups",
             "Your 2FA secrets are stored only on your device. We cannot see, restore or recover them. If you "
             "lose your device or delete the app without a backup, you may lose access to your accounts. Keep "
             "an encrypted backup and the recovery codes each service gives you."),
        ],
    ),
]

CSS_LINK = '<link rel="stylesheet" href="{p}assets/site.css">'


def head(title, desc, prefix):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
{CSS_LINK.format(p=prefix)}
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="{prefix}index.html">TGS Mobile Apps</a>
  <nav><a href="{prefix}index.html#apps">Apps</a><a href="{prefix}support.html">Support</a><a href="{prefix}privacy-policy.html">Privacy</a></nav>
</div></header>
"""


def foot(prefix):
    return f"""<footer><div class="wrap">
  <p>© 2026 TGS Mobile Apps · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p><a href="{prefix}privacy-policy.html">Privacy Policy</a> · <a href="{prefix}support.html">Support</a></p>
</div></footer>
</body>
</html>
"""


def badges(a):
    if not a["ios"] and not a["play"]:
        return '<span class="soon">Coming soon</span>'
    out = []
    if a["ios"]:
        out.append(f'<a class="store" href="{a["ios"]}">App Store</a>')
    if a["play"]:
        out.append(f'<a class="store" href="{a["play"]}">Google Play</a>')
    return "".join(out)


def index():
    cards = "\n".join(f"""  <article class="card">
    <img src="assets/icons/{a['icon']}" alt="" width="72" height="72">
    <div>
      <h3>{escape(a['name'])}</h3>
      <p>{escape(a['tagline'])}</p>
      <div class="links">{badges(a)}</div>
      <p class="small"><a href="terms/{a['slug']}.html">Terms of Service</a> · <a href="privacy-policy.html">Privacy</a></p>
    </div>
  </article>""" for a in APPS)
    return head("TGS Mobile Apps", "Small, useful mobile apps for health, home and security.", "") + f"""<main>
<section class="hero"><div class="wrap">
  <h1>Small apps that do one job well.</h1>
  <p>TGS Mobile Apps builds focused iPhone and Android apps for family health, home organization, plants and account security.</p>
</div></section>
<section class="wrap" id="apps">
  <h2>Our apps</h2>
  <div class="grid">
{cards}
  </div>
</section>
<section class="wrap contact">
  <h2>Contact</h2>
  <p>Questions, feedback or a problem with an app? Write to <a href="mailto:{EMAIL}">{EMAIL}</a>. We usually reply within two business days.</p>
</section>
</main>
""" + foot("")


def terms(a):
    n = escape(a["name"])
    sections = [
        ("1. Who we are",
         f"{n} (the \"App\") is published by {OWNER} (\"we\", \"us\"). You can reach us at "
         f"<a href=\"mailto:{EMAIL}\">{EMAIL}</a>. By downloading or using the App you agree to these Terms. "
         "If you do not agree, do not use the App."),
        ("2. What the App does",
         f"The App {escape(a['what'])}. Features can change between versions."),
        ("3. Licence",
         "We give you a personal, non-exclusive, non-transferable licence to use the App on devices you own or "
         "control, under the rules of the App Store or Google Play you got it from. You may not copy, resell, "
         "reverse engineer or misuse the App, or use it for anything unlawful."),
    ]
    if a["account"]:
        sections.append(("4. Your account",
            "Some features need an account. Keep your sign-in details secure and give accurate information. You "
            "can delete your account from the App's settings; see our Privacy Policy for what happens to your data."))
    if a["ai"]:
        sections.append(("AI features",
            "Parts of the App use artificial intelligence (Google Gemini) to analyse photos or text you choose to "
            "send. AI results can be incomplete or wrong. Check important results yourself and do not rely on "
            "them alone."))
    if a["medical"]:
        sections.append(("Not medical advice",
            "The App is for record keeping and reminders only. It does not provide medical advice, diagnosis or "
            "treatment and does not replace a doctor, pharmacist or other healthcare professional. In an "
            "emergency, contact your local emergency number."))
    sections += [(t, escape(b)) for t, b in a["extra"]]
    sections += [
        ("Subscriptions and payments",
         "The App can be used for free with limits. Optional premium features are offered as auto-renewing "
         "subscriptions sold through the App Store or Google Play. Prices, the billing period and any free "
         "trial are shown before you buy. Payment is taken by Apple or Google. A subscription renews "
         "automatically unless you cancel at least 24 hours before the current period ends (Apple) or before "
         "the renewal date (Google Play). You can manage or cancel it in your App Store or Google Play account "
         "settings; deleting the App does not cancel it. Refunds are handled by Apple or Google under their "
         "policies."),
        ("Your content",
         "Photos, notes and other content you add stay yours. You give us only the rights needed to run the "
         "features you use, for example sending a photo for AI analysis. Our "
         "<a href=\"../privacy-policy.html\">Privacy Policy</a> explains what we collect and how."),
        ("Availability and data",
         "We work to keep the App running and your data safe, but we cannot promise it will always be available "
         "or error-free. Keep copies of anything important."),
        ("Liability",
         "The App is provided \"as is\". To the extent the law allows, we are not liable for indirect or "
         "consequential losses, or for decisions made based on the App's content. Nothing in these Terms limits "
         "liability that cannot be limited by law, or your statutory rights as a consumer, including your rights "
         "under the consumer laws of the country where you live."),
        ("Apple-specific terms",
         "If you got the App from the App Store, Apple's standard "
         "<a href=\"https://www.apple.com/legal/internet-services/itunes/dev/stdeula/\">Licensed Application End "
         "User License Agreement</a> also applies. Apple is not responsible for the App or its support."),
        ("Changes and ending use",
         "We may update these Terms; the date at the top shows the latest version, and important changes may be "
         "announced in the App. You can stop using the App at any time by deleting it. We may suspend access if "
         "these Terms are seriously breached."),
        ("Governing law",
         "These Terms are governed by the laws of the Republic of Türkiye. If you are a consumer living in "
         "another country, you also keep the protection of the mandatory laws of that country."),
        ("Contact",
         f"Questions about these Terms: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>."),
    ]
    # Sıra numaralarını yeniden ver (koşullu bölümler araya girebiliyor)
    body = "\n".join(
        f"<h2>{i}. {t.split('. ', 1)[-1]}</h2>\n<p>{b}</p>" for i, (t, b) in enumerate(sections, 1))
    return head(f"Terms of Service – {a['name']}", f"Terms of Service for {a['name']}", "../") + f"""<main class="wrap doc">
<p class="crumb"><a href="../index.html#apps">Apps</a> › {n}</p>
<h1>Terms of Service</h1>
<p class="lead">{n}<br><span class="small">Last updated: {UPDATED}</span></p>
{body}
</main>
""" + foot("../")


(ROOT / "index.html").write_text(index(), encoding="utf-8")
(ROOT / "terms").mkdir(exist_ok=True)
for a in APPS:
    (ROOT / "terms" / f"{a['slug']}.html").write_text(terms(a), encoding="utf-8")
print("ok:", 1 + len(APPS), "pages")
