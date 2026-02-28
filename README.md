# ВЕМА 2005 ООД — Website

Corporate website for **ВЕМА 2005 ООД**, an engineering firm based in Sofia, Bulgaria, specialising in structured cabling systems, pump stations, and industrial automation.

---

## Pages

| File | Description |
|---|---|
| `index.html` | Homepage — company overview and service categories |
| `clients.html` | Full client list (65+ organisations) |
| `contacts.html` | Contact details and embedded Google Maps location |

---

## Tech Stack

Plain HTML and CSS — no frameworks, no build tools, no dependencies. The only external resources loaded are:

- **Google Fonts** — DM Serif Display + DM Sans (via `fonts.googleapis.com`)
- **Google Maps Embed API** — iframe embed on the contacts page

---

## Structure

```
/
├── index.html
├── clients.html
├── contacts.html
└── static/
    └── logo/
        └── vema-logo-long.png
    └── css/
        └── stylesheet.css
```

---

## Development

No build step required. Open any `.html` file directly in a browser, or serve locally with any static file server.

---

## Deployment

The site is static and can be hosted on any platform that serves HTML files — Apache, Nginx, GitHub Pages, Netlify, Vercel, etc. No server-side processing is required.

---

## Contact

**ВЕМА 2005 ООД**
ул. Родопски Извор 3, гр. София
vema2005@abv.bg
