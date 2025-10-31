# ctodd.com - Personal Website

A modern, Flask-based personal website with integrated Substack blog feed.

## Features

- 🎨 Clean, modern design with responsive layout
- 📝 Automatic Substack RSS feed integration
- 🚀 Easy deployment to Railway, Render, or Heroku
- 📱 Mobile-friendly
- ⚡ Fast and lightweight

## Project Structure

```
ctodd.com/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   └── 404.html
└── static/              # Static files
    ├── css/
    │   └── style.css
    ├── js/
    └── images/
```

## Local Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ctodd.com
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your Substack URL
   ```

5. **Run the development server**
   ```bash
   python app.py
   ```

   Visit `http://localhost:5000` in your browser.

## Configuration

Update the following in `app.py` or your `.env` file:

- `SUBSTACK_URL`: Your Substack RSS feed URL (e.g., `https://yourusername.substack.com/feed`)
- `SUBSTACK_BLOG_URL`: Your Substack blog URL (e.g., `https://blog.ctodd.com` or `https://yourusername.substack.com`)

## Customization

### Update Personal Information

1. **About Page**: Edit `templates/about.html`
   - Add your bio
   - Update skills and technologies
   - Add your email and social links

2. **Projects**: Edit `templates/projects.html`
   - Add your projects with images, descriptions, and links

3. **Navigation Links**: Edit `templates/base.html`
   - Update social media links in the footer
   - Adjust navigation items if needed

4. **Colors & Styling**: Edit `static/css/style.css`
   - Modify CSS variables at the top of the file for colors
   - Adjust fonts, spacing, etc.

### Add Your Profile Photo

Place your profile photo at `static/images/profile.jpg`

## Deployment

### Railway (Recommended)

1. Create a new project on [Railway](https://railway.app/)
2. Connect your GitHub repository
3. Add environment variables in Railway dashboard:
   - `SUBSTACK_URL`
   - `SUBSTACK_BLOG_URL`
4. Deploy! Railway will automatically detect Flask and deploy

## Setting Up Custom Domain with Substack

To use `blog.ctodd.com` for your Substack:

1. Upgrade to Substack Pro ($10/month)
2. Go to Settings → Publishing → Domain
3. Add your custom domain
4. Create a CNAME record in your DNS:
   - Name: `blog`
   - Value: (provided by Substack)

## Development

### Testing RSS Feed Integration

The app fetches posts from Substack's RSS feed. To test:

```python
python -c "from app import get_latest_posts; print(get_latest_posts())"
```

### Adding New Routes

Add new routes in `app.py`:

```python
@app.route('/new-page')
def new_page():
    return render_template('new_page.html')
```

## Troubleshooting

**Posts not showing up?**
- Check that your Substack URL is correct
- Ensure your Substack has published posts
- Check the browser console for errors

**Styling issues?**
- Clear browser cache
- Check that `style.css` is loading correctly

## License

MIT License - feel free to use this for your own personal website!

## Contact

Questions? Reach out at hello@ctodd.com
