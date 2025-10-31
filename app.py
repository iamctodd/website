import ssl
import urllib.request
from flask import Flask, render_template, redirect
import feedparser
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['SUBSTACK_URL'] = 'https://ctodd.substack.com/feed'  # Update with your actual Substack URL
app.config['SUBSTACK_BLOG_URL'] = 'https://ctodd.substack.com'

def get_latest_posts(limit=3):
    """Fetch latest posts from Substack RSS feed"""
    try:
        # Bypass SSL verification
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        
        # Parse the feed with SSL context
        feed = feedparser.parse(app.config['SUBSTACK_URL'], handlers=[urllib.request.HTTPSHandler(context=ssl_context)])
        print(f"Number of entries found: {len(feed.entries)}")
        
        if len(feed.entries) == 0:
            print("WARNING: No entries found in feed!")
            return []
        
        posts = []
        for entry in feed.entries[:limit]:
            print(f"Processing entry: {entry.title}")
            published = datetime(*entry.published_parsed[:6])
            summary = entry.get('summary', '')
            if len(summary) > 200:
                summary = summary[:200] + '...'
            posts.append({
                'title': entry.title,
                'link': entry.link,
                'summary': summary,
                'published': published.strftime('%B %d, %Y'),
                'published_date': published
            })
        print(f"Returning {len(posts)} posts")
        return posts
    except Exception as e:
        print(f"Error fetching Substack posts: {e}")
        import traceback
        traceback.print_exc()
        return []
@app.route('/')
def index():
    """Homepage with latest blog posts"""
    latest_posts = get_latest_posts(3)
    return render_template('index.html', posts=latest_posts)

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/projects')
def projects():
    """Projects showcase page"""
    return render_template('projects.html')

@app.route('/writing')
def writing():
    """Redirect to Substack blog"""
    return redirect(app.config['SUBSTACK_BLOG_URL'])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=8675)  # Change to 5001 if port in use
