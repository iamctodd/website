# Quick Reference Guide

## Common Tasks

### Starting Development Server
```bash
python app.py
```
Visit: `http://localhost:5000`

### Installing Dependencies
```bash
pip install -r requirements.txt
```

### Project Structure Quick Reference

```
ctodd.com/
├── app.py                      # Main Flask app - add routes here
├── requirements.txt            # Python packages
├── Procfile                    # Heroku deployment config
├── .env.example               # Environment variables template
├── templates/
│   ├── base.html              # Main layout (nav, footer)
│   ├── index.html             # Homepage with blog feed
│   ├── about.html             # About page - edit your bio here
│   ├── projects.html          # Projects showcase
│   └── 404.html               # Error page
└── static/
    ├── css/
    │   └── style.css          # All styling - edit colors here
    ├── js/                    # Your JavaScript files
    └── images/                # Put profile.jpg here
```

## Customization Quick Hits

### Change Colors
Edit `static/css/style.css` - lines 14-21:
```css
:root {
    --primary-color: #2563eb;    /* Main brand color */
    --text-color: #1e293b;       /* Body text */
    --bg-color: #ffffff;         /* Background */
}
```

### Add New Page
1. Create template: `templates/newpage.html`
2. Add route in `app.py`:
```python
@app.route('/newpage')
def newpage():
    return render_template('newpage.html')
```
3. Add to navigation in `templates/base.html`

### Update Social Links
Edit `templates/base.html` - lines 35-39 (footer section)

### Modify Substack Settings
Edit `app.py` - lines 9-10:
```python
app.config['SUBSTACK_URL'] = 'https://substack.com/@iamctodd'
app.config['SUBSTACK_BLOG_URL'] = 'https://substack.com/@iamctodd'
```

## File Locations Cheat Sheet

| What to Edit | Where to Find It |
|--------------|------------------|
| Your bio | `templates/about.html` |
| Projects | `templates/projects.html` |
| Hero text | `templates/index.html` |
| Navigation | `templates/base.html` |
| Footer | `templates/base.html` |
| Colors/fonts | `static/css/style.css` |
| Substack URL | `app.py` or `.env` |
| Profile photo | `static/images/profile.jpg` |
| Social links | `templates/base.html` (footer) |

## Key URLs in Your Site

| Page | Route | Template |
|------|-------|----------|
| Homepage | `/` | `index.html` |
| About | `/about` | `about.html` |
| Projects | `/projects` | `projects.html` |
| Writing | `/writing` | Redirects to Substack |

## Environment Variables

Create `.env` file with:
```
FLASK_APP=app.py
FLASK_ENV=development
SUBSTACK_URL=https://yoursubstack.com/feed
SUBSTACK_BLOG_URL=https://blog.ctodd.com
```

## Deployment Commands

### Railway
```bash
# Railway auto-deploys from GitHub
# Just push to main branch
git push origin main
```

### Heroku
```bash
heroku create
git push heroku main
heroku config:set SUBSTACK_URL=your-url
```

## Testing Substack Integration

Test if RSS feed works:
```python
python -c "from app import get_latest_posts; print(get_latest_posts())"
```

## Common Issues & Fixes

**Posts not showing?**
- Check Substack URL in `.env` or `app.py`
- Make sure Substack blog has published posts

**CSS not working?**
- Hard refresh: Ctrl+Shift+R (Cmd+Shift+R on Mac)
- Check file path: `{{ url_for('static', filename='css/style.css') }}`

**Page not found?**
- Check route in `app.py`
- Verify template filename matches

## Git Commands Cheat Sheet

```bash
git status                  # Check what changed
git add .                   # Stage all changes
git commit -m "message"     # Commit changes
git push                    # Push to GitHub
```

## Useful Flask Template Syntax

```html
<!-- Link to static file -->
<img src="{{ url_for('static', filename='images/photo.jpg') }}">

<!-- Link to route -->
<a href="{{ url_for('about') }}">About</a>

<!-- Loop through posts -->
{% for post in posts %}
    <h3>{{ post.title }}</h3>
{% endfor %}

<!-- Conditional -->
{% if user_logged_in %}
    <p>Welcome!</p>
{% endif %}
```

## Need More Help?

- Full docs: See `README.md`
- Deployment: See `DEPLOYMENT_CHECKLIST.md`
- Flask docs: https://flask.palletsprojects.com/
- Railway docs: https://docs.railway.app/
