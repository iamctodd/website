# 🚀 Deployment Checklist for ctodd.com

## Pre-Deployment Customization

### Required Changes
- [ ] Update Substack URL in `app.py` or `.env` (line 9)
- [ ] Update email in `templates/about.html` (replace `hello@ctodd.com`)
- [ ] Add your bio and information in `templates/about.html`
- [ ] Add your real projects in `templates/projects.html`
- [ ] Update social media links in `templates/base.html` (footer section)
- [ ] Add your profile photo to `static/images/profile.jpg`

### Optional Customizations
- [ ] Change color scheme in `static/css/style.css` (CSS variables at top)
- [ ] Update site title in `templates/base.html`
- [ ] Modify hero text in `templates/index.html`
- [ ] Add Google Analytics (if desired)
- [ ] Add favicon

## Local Testing

- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Copy `.env.example` to `.env` and update values
- [ ] Run locally: `python app.py`
- [ ] Test all pages:
  - [ ] Homepage (/)
  - [ ] About (/about)
  - [ ] Projects (/projects)
  - [ ] Writing redirect (/writing)
- [ ] Verify Substack posts appear on homepage
- [ ] Test mobile responsiveness

## Git Setup

- [ ] Initialize git repository: `git init`
- [ ] Add all files: `git add .`
- [ ] Commit: `git commit -m "Initial commit"`
- [ ] Create GitHub repository
- [ ] Push to GitHub:
  ```bash
  git remote add origin https://github.com/yourusername/ctodd.com.git
  git branch -M main
  git push -u origin main
  ```

## Railway Deployment (Recommended)

- [ ] Sign up at [Railway.app](https://railway.app)
- [ ] Click "New Project" → "Deploy from GitHub repo"
- [ ] Select your repository
- [ ] Add environment variables:
  - `SUBSTACK_URL`: Your Substack RSS feed
  - `SUBSTACK_BLOG_URL`: Your Substack blog URL
- [ ] Railway auto-detects Flask and deploys
- [ ] Get your Railway URL (e.g., `your-app.railway.app`)
- [ ] Test the live site

## Custom Domain Setup

### For Main Site (ctodd.com)
- [ ] In Railway: Settings → Domains → Add Custom Domain
- [ ] Add DNS records at your domain registrar:
  - Type: `A` or `CNAME`
  - Name: `@` (or blank)
  - Value: (provided by Railway)
- [ ] Add www subdomain (optional):
  - Type: `CNAME`
  - Name: `www`
  - Value: `ctodd.com`

### For Substack (blog.ctodd.com)
- [ ] Upgrade to Substack Pro ($10/month)
- [ ] In Substack: Settings → Publishing → Domain
- [ ] Add custom domain: `blog.ctodd.com`
- [ ] Add DNS record at your domain registrar:
  - Type: `CNAME`
  - Name: `blog`
  - Value: (provided by Substack)
- [ ] Update `SUBSTACK_BLOG_URL` in Railway to `https://blog.ctodd.com`

## Post-Deployment

- [ ] Test all pages on live site
- [ ] Verify Substack integration works
- [ ] Test mobile responsiveness
- [ ] Share your new site! 🎉

## Alternative Deployment Options

### Render
- Similar to Railway
- Go to [Render.com](https://render.com)
- Create new Web Service from GitHub
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

### Heroku
- Install Heroku CLI
- `heroku create ctodd-website`
- `git push heroku main`
- `heroku config:set SUBSTACK_URL=your-url`

## Troubleshooting

**Posts not showing:**
- Check Substack URL is correct
- Verify Substack has published posts
- Check browser console for errors

**Site not loading:**
- Check Railway logs
- Verify environment variables are set
- Ensure requirements.txt includes all dependencies

**CSS not loading:**
- Clear browser cache
- Check static file paths
- Verify deployment completed successfully

## Maintenance

- [ ] Set up monitoring (Railway provides basic monitoring)
- [ ] Regularly update dependencies
- [ ] Back up your content
- [ ] Consider adding SSL certificate (automatic with Railway/Render)

---

Need help? Check the README.md for more detailed instructions!
