<p align="center">
  <img src="https://github.com/user-attachments/assets/6ce54a27-8fb6-48e6-9d1f-da144f43425a"/>
</p>

<h3 align="center">cryptnox-readers</h3>
<p align="center">Compatibility documentation for Cryptnox USB smart card readers</p>

<br/>
<br/>

[![docs](https://github.com/cryptnox/cryptnox-readers/actions/workflows/deploy.yml/badge.svg)](https://github.com/cryptnox/cryptnox-readers/actions/workflows/deploy.yml)
[![License: LGPLv3](https://img.shields.io/badge/License-LGPLv3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

Documentation for the **Cryptnox USB smart card readers**: which national eID
and professional cards work with them, country by country; which services and
platforms work with a Cryptnox FIDO2 card; and what the Click-to-Tap button
does.

Published at
[docs.cryptnox.com/cryptnox-readers](https://docs.cryptnox.com/cryptnox-readers/),
part of the [Cryptnox documentation portal](https://docs.cryptnox.com).

---

## Contents

| Article | What it answers |
|---------|-----------------|
| **Smart Card Reader Compatibility by Country** | National eID and professional card compatibility per country, with the official government middleware required for each |
| **FIDO2 Card Compatibility — Services and Platforms** | Which services and operating systems work with a Cryptnox FIDO2 NFC card, second-factor or passwordless, and where extra software is needed |
| **Click-to-Tap — FIDO2 User Presence on a Desktop Reader** | What the Click-to-Tap button does, why FIDO2 sign-in on a contact reader needs it, its requirements, and troubleshooting |

A single PDF of all articles is built with every deploy and linked from the
site's index page.

---

## The readers

| Reader | Type | Connector |
|--------|------|-----------|
| [Cryptnox® Smartcard Reader](https://shop.cryptnox.com/product/cryptnox-smartcard-reader/) | Contact (ISO/IEC 7816, T=0/T=1) | USB-C, USB-A adapter supplied |
| [Cryptnox NFC Contactless Reader](https://shop.cryptnox.com/product/cryptnox-contactless-reader/) | Contactless (ISO/IEC 14443 A/B) | USB-C, USB-A adapter supplied |

Both support extended APDU, which national eID schemes and ICAO 9303 travel
documents require for certificates and signatures larger than the 255/256-byte
short-APDU limit.

---

## Building locally

```bash
pip install -r requirements.txt
sphinx-build -W -b html docs/source docs/_build/html
```

For the PDF (requires a LaTeX installation with latexmk):

```bash
sphinx-build -M latexpdf docs/source docs/_build
```

---

## Get your hardware

Cryptnox smart cards and compatible readers are available at
[shop.cryptnox.com](https://shop.cryptnox.com).
