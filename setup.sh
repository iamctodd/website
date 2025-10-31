#!/bin/bash

echo "🚀 ctodd.com Setup Script"
echo "========================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "✅ Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "⚙️  Creating .env file..."
    cp .env.example .env
    echo "⚠️  Please edit .env with your Substack URL!"
fi

echo ""
echo "✨ Setup complete!"
echo ""
echo "To start the development server:"
echo "  1. Activate virtual environment: source venv/bin/activate"
echo "  2. Run: python app.py"
echo "  3. Visit: http://localhost:5000"
echo ""
echo "Don't forget to:"
echo "  - Update .env with your Substack URL"
echo "  - Customize templates/about.html"
echo "  - Add your projects to templates/projects.html"
echo "  - Add your profile photo to static/images/profile.jpg"
