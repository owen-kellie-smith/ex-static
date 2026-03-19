# EX Summer School – Static Site

Plain static HTML site served via GitHub Pages using Jekyll.

https://owen-kellie-smith.github.io/ex-static/


---

You can edit any page directly on GitHub — no software needed.

**How to edit a file (if you are the repo owner):**
1. Find the page 
2. Click the **pencil icon** (✏️) in the top-right of the file view
3. Make your changes
4. Click **Commit changes**

The site updates automatically within a minute or two.

**How to change something (if you are not the repo owner):**
1. Raise an [issue](https://github.com/owen-kellie-smith/ex-static/issues) i.e. describe what you want, or
2. Fork the repo (make a copy that you control)
3. Edit the fork.
4. Render the fork by creating a page (Settings -> Pages) running from your repo's root directory
5. Create a pull request (that your changes be incorporated into the main site).

**How to render the site on command line:**

`jekyll serve`

and then browse to

`http://localhost:4000`


---


## 🗂️ File structure

```
*.md                    – Page content
assets/                 – photos and PDFs
  style.css             – Shared styles
_layout			- Page format
_includes		- Header and footer
```

---

## 🚀 GitHub Pages setup (first time only)

1. Push this folder to a GitHub repository
2. Go to **Settings → Pages**
3. Set source to **main branch / root folder**
4. Site goes live at `https://<username>.github.io/<repo>/` ie in this case at `https://owen-kellie-smith.github.io/ex-static/`


## Cloudflare settings

See https://github.com/owen-kellie-smith/etcb-website?tab=readme-ov-file#cloudflare-settings
