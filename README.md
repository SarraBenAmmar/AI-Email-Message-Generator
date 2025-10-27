🚀 AI Email & Content Generator
<div align="center">
https://img.shields.io/badge/Frontend-React-61DBFB?logo=react&logoColor=white
https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi&logoColor=white
https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white
https://img.shields.io/badge/Language-JavaScript-F7DF1E?logo=javascript&logoColor=black
https://img.shields.io/badge/License-MIT-green

A powerful AI-powered content generation platform built with modern technologies

</div>
✨ About The Project
AI Email & Content Generator is a cutting-edge web application that leverages OpenRouter AI with the Mistral model to create high-quality, context-aware content across multiple formats. Whether you need professional communications or creative content, this tool streamlines your writing process with AI-powered assistance.

🎯 Key Features
📧 Smart Email Composition - Generate professional emails for business, marketing, or personal use

📱 Social Media Content - Create engaging posts for platforms like Twitter, LinkedIn, and Instagram

🎬 Video Scripts - Develop compelling scripts for YouTube and other video content

💡 Creative Brainstorming - Generate ideas, messages, and creative content on demand

⚡ Real-time Generation - Instant AI responses with a modern, intuitive interface

🎨 Futuristic UI - Beautiful glowing design with smooth user experience

🖼️ Application Preview
<div align="center">
https://github.com/user-attachments/assets/0729fd7d-f845-4473-a574-129020aacc7f

Modern dashboard with glowing effects and real-time content generation

</div>
🏗️ Project Architecture
Technology Stack
Layer	Technology	Purpose
Frontend	React.js	Modern, responsive user interface
Backend	FastAPI (Python)	High-performance API server
AI Integration	OpenRouter API	Access to Mistral and other AI models
Styling	CSS3 with modern effects	Futuristic glowing UI design
Project Structure
bash
ai-email-generator/
│
├── 📁 frontend/                 # React Application
│   ├── src/
│   │   ├── components/         # Reusable UI components
│   │   ├── services/          # API integration services
│   │   ├── styles/            # CSS and styling files
│   │   └── utils/             # Helper functions
│   ├── public/                # Static assets
│   └── package.json           # Dependencies and scripts
│
├── 📁 backend/                # FastAPI Server
│   ├── main.py               # Main application file
│   ├── config.py             # Configuration settings
│   ├── services/             # Business logic and AI integration
│   ├── models/               # Data models
│   ├── requirements.txt      # Python dependencies
│   └── .env.example          # Environment variables template
│
└── 📄 README.md              # Project documentation
🚀 Quick Start Guide
Prerequisites
Before you begin, ensure you have the following installed:

Node.js (version 14 or higher)

Python (version 3.8 or higher)

pip (Python package manager)

Step 1: Clone the Repository
bash
# Clone the project
git clone https://github.com/YOUR-USERNAME/ai-email-generator.git

# Navigate to project directory
cd ai-email-generator
Step 2: Backend Setup (FastAPI)
Navigate to backend directory:

bash
cd backend
Create and activate virtual environment:

bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
Install Python dependencies:

bash
pip install -r requirements.txt
Set up environment variables:

Copy .env.example to .env

Add your OpenRouter API key:

text
OPENROUTER_API_KEY=your_api_key_here
Start the backend server:

bash
python main.py
✅ Backend running at: http://localhost:8000

Step 3: Frontend Setup (React)
Open a new terminal and navigate to frontend:

bash
cd frontend
Install Node.js dependencies:

bash
npm install
Start the React development server:

bash
npm start
✅ Frontend running at: http://localhost:3000

🔧 Configuration
Environment Variables
Create a .env file in the backend directory with the following variables:

env
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_MODEL=mistralai/mistral-7b-instruct
API_HOST=localhost
API_PORT=8000
FRONTEND_URL=http://localhost:3000
Getting Your API Key
Visit OpenRouter

Create an account and generate an API key

Copy the key into your .env file

💻 Usage Guide
Generating Content
Select Content Type - Choose from email, social media, scripts, or creative content

Provide Context - Enter your topic, tone, and any specific requirements

Generate - Click the generate button for instant AI-powered content

Copy & Use - Copy the generated content directly to your applications

Available Content Types
Content Type	Best For	Example Use Cases
Professional Email	Business communication	Sales pitches, follow-ups, introductions
Social Media Post	Engagement content	Twitter threads, LinkedIn posts, Instagram captions
Video Script	Content creation	YouTube videos, tutorials, presentations
Creative Ideas	Brainstorming	Marketing campaigns, project ideas, content planning
🛠️ API Endpoints
Content Generation
http
POST /api/generate
Content-Type: application/json

{
  "content_type": "email",
  "topic": "Follow-up meeting",
  "tone": "professional",
  "additional_context": "Need to follow up on last week's discussion"
}
Health Check
http
GET /api/health
Returns API status and version information

🔒 Security Features
API Key Protection - Secure handling of AI service credentials

Input Validation - Comprehensive validation of all user inputs

CORS Configuration - Proper cross-origin resource sharing settings

Error Handling - Graceful error management without exposing sensitive data

🤝 Contributing
We welcome contributions! Please follow these steps:

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

Development Guidelines
Follow PEP 8 for Python code

Use ESLint for JavaScript/React code

Write meaningful commit messages

Update documentation for new features

📝 Troubleshooting
Common Issues
Backend won't start:

Verify Python version (3.8+ required)

Check if virtual environment is activated

Ensure all dependencies are installed

Frontend connection issues:

Confirm backend is running on port 8000

Check CORS configuration

Verify API endpoints in frontend services

API key errors:

Ensure OpenRouter API key is valid

Check .env file location and formatting

Verify account credits on OpenRouter

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Sara Ben Ammar

GitHub: @YourUsername

Email: sarrahhbam@gmail.com

🙏 Acknowledgments
OpenRouter for providing AI model access

Mistral AI for the powerful language model

React & FastAPI communities for excellent documentation and support

<div align="center">
Ready to create amazing content? 🚀
Star this repository if you find it helpful!

</div>
🔄 Future Enhancements
Template library for common content types

Content history and saving functionality

Multiple AI model support

Export functionality (PDF, DOCX)

Team collaboration features

Advanced customization options

