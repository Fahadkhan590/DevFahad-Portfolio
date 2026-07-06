# DevFahad — Portfolio (Streamlit)

A professional, modern, mobile-first, dark-mode one-page portfolio built with Streamlit.

## 🚀 Run Locally

```bash
# 1. Install dependency
pip install -r requirements.txt

# 2. Launch the app (image_3.png must sit next to app.py)
streamlit run app.py
```

The site will open at **http://localhost:8501**.

## 📁 Files

| File | Description |
|------|-------------|
| `app.py` | Full single-page portfolio (all sections + custom CSS) |
| `image_3.png` | Profile portrait, loaded via `st.image()` at 300px |
| `requirements.txt` | Python dependencies |

## 🎨 Sections

1. **Sticky Nav** — Brand + jump links (About / Skills / Projects / Contact)
2. **Hero** — 300px profile photo (gradient ring) + name, tagline, Peshawar location
3. **About** — Short intro on AI-augmented development
4. **Skills** — 4-card grid (UI/UX · Web · eCommerce · Game Dev with CodeWisp & Arena AI)
5. **Projects** — Two rich cards for `toolboxtools.netlify.app` & `fincalchub.xyz` (Role, Goal, Impact)
6. **Contact** — Email · GitHub · YouTube · WhatsApp buttons (all with real links)

## 🌐 Deploy

Push to GitHub (including `image_3.png`) and deploy free on **[Streamlit Community Cloud](https://streamlit.io/cloud)** — point it at `app.py` and you're live.

## ✏️ Customize

- **Colors** — tweak the gradients in the `<style>` block (indigo `#6366f1` + emerald `#10b981`).
- **Content** — every text block is plain HTML inside `st.markdown(...)`, easy to edit.
- **Photo** — replace `image_3.png` with any square/portrait PNG.
