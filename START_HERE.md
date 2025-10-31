# 🎉 Getting Started with Your New Site

Welcome to your new Flask-powered personal website with Substack integration!

## What You Just Got

✨ A complete, production-ready Flask website including:
- Modern, responsive design
- Homepage with automatic Substack blog previews
- About page for your bio
- Projects showcase page
- Automatic integration with your Substack blog
- Ready to deploy to Railway, Render, or Heroku

## First Steps (5 minutes)

### 1. Download All Files
All your files are ready in the outputs folder. Download them to your computer.

### 2. Set Up Locally

**IMPORTANT:** You must install dependencies before running the app!

**Option A: Use the setup script (Easiest)**
```bash
# macOS/Linux:
chmod +x start.sh
./start.sh

# Windows:
start.bat
```

**Option B: Manual setup**
```bash
# Navigate to your project folder
cd ctodd.com

# Create virtual environment
python3 -m venv venv  # macOS/Linux
python -m venv venv   # Windows

# Activate virtual environment
source venv/bin/activate              # macOS/Linux
venv\Scripts\activate                 # Windows CMD
venv\Scripts\Activate.ps1             # Windows PowerShell

# Install dependencies (REQUIRED!)
pip install -r requirements.txt

# Create environment file
cp .env.example .env    # macOS/Linux
copy .env.example .env  # Windows
```

**Verify installation worked:**
```bash
pip list
# You should see: Flask, feedparser, gunicorn, python-dotenv
```

### 3. Configure Your Substack
Edit `.env` or `app.py` (line 9-10):
```python
SUBSTACK_URL = 'https://yourname.substack.com/feed'
SUBSTACK_BLOG_URL = 'https://yourname.substack.com'
```

### 4. Test It Out
```bash
python app.py
```
Visit `http://localhost:6000` - you should see your site!

## Next Steps (30 minutes)

### Customize Your Content

1. **About Page** (`templates/about.html`)
   - Add your bio
   - Update skills and technologies
   - Change email address
   - Add social media links

2. **Projects Page** (`templates/projects.html`)
   - Replace placeholder projects with your real work
   - Add project images
   - Link to live demos and GitHub repos

3. **Homepage** (`templates/index.html`)
   - Customize the hero text
   - Adjust the call-to-action buttons

4. **Add Your Photo**
   - Add `profile.jpg` to `static/images/`

### Optional Styling

Edit `static/css/style.css` to change:
- Colors (lines 14-21)
- Fonts
- Spacing
- Anything else!

## Deploy to Railway (15 minutes)

Railway is the easiest deployment option:

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/ctodd.com.git
   git push -u origin main
   ```

2. **Deploy on Railway**
   - Go to [railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Add environment variables:
     - `SUBSTACK_URL`
     - `SUBSTACK_BLOG_URL`
   - Railway auto-deploys!

3. **Get Your URL**
   - Railway gives you a URL like `your-app.railway.app`
   - Visit it to see your live site!

## Set Up Custom Domain (30 minutes)

### For Your Main Site (ctodd.com)

1. **In Railway**:
   - Settings → Domains → Add Custom Domain
   - Enter `ctodd.com`

2. **In Your Domain Registrar** (GoDaddy, Namecheap, etc.):
   - Add A record or CNAME as instructed by Railway
   - Usually takes 24-48 hours to propagate

### For Your Blog (blog.ctodd.com)

1. **Upgrade to Substack Pro** ($10/month)
   - Needed for custom domains

2. **In Substack**:
   - Settings → Publishing → Domain
   - Add `blog.ctodd.com`

3. **In Your Domain Registrar**:
   - Add CNAME record:
     - Name: `blog`
     - Value: (provided by Substack)

4. **Update Your Config**:
   - Change `SUBSTACK_BLOG_URL` to `https://blog.ctodd.com`
   - Redeploy on Railway

## What to Do Next

### Start Writing on Substack
1. Go to your Substack dashboard
2. Write and publish posts
3. They'll automatically appear on your homepage!

### Share Your Site
- Update your social media bios
- Add your site to your email signature
- Share on LinkedIn, Twitter, etc.

### Keep Building
Some ideas:
- Add a contact form
- Create more project pages
- Add a newsletter signup
- Integrate analytics
- Add a blog archive page

## Important Files Reference

| File | What It Does |
|------|--------------|
| `app.py` | Main Flask application |
| `templates/` | All HTML pages |
| `static/css/style.css` | All styling |
| `requirements.txt` | Python dependencies |
| `.env` | Configuration (don't commit this!) |
| `Procfile` | Deployment config |

## Helpful Documents

📚 **Detailed Guides**:
- `README.md` - Complete documentation
- `ARCHITECTURE.md` - How everything works together
- `DEPLOYMENT_CHECKLIST.md` - Step-by-step deployment guide
- `QUICK_REFERENCE.md` - Common tasks and commands

## Getting Help

### Common Issues

**Posts not showing up?**
- Check your Substack URL is correct
- Make sure you have published posts on Substack
- Try fetching the RSS feed manually

**Site looks broken?**
- Hard refresh your browser (Ctrl+Shift+R)
- Check browser console for errors
- Verify all files uploaded correctly

**Can't deploy?**
- Check all files are committed to git
- Verify environment variables are set
- Check Railway/Render logs for errors

### Resources

- Flask documentation: https://flask.palletsprojects.com/
- Railway docs: https://docs.railway.app/
- Substack help: https://support.substack.com/
- Tailwind CSS (if you want to add it): https://tailwindcss.com/

## Timeline Summary

- **5 min**: Download and set up locally ✅
- **30 min**: Customize content ✅
- **15 min**: Deploy to Railway ✅
- **30 min**: Set up custom domain ✅
- **∞**: Keep building and writing! 🚀

## You're All Set! 🎊

You now have:
- ✅ A professional personal website
- ✅ Automatic blog integration
- ✅ Easy deployment pipeline
- ✅ Custom domain ready
- ✅ Complete control over your content

Start customizing and make it your own!

Questions? Check the README.md or the other documentation files.

**Happy building! 🚀**