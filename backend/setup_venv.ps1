# PowerShell script to set up isolated virtual environment
Write-Host "Setting up isolated Python environment..." -ForegroundColor Green

# Create virtual environment
python -m venv venv_ai_email

# Activate virtual environment
.\venv_ai_email\Scripts\Activate.ps1

# Upgrade pip
python -m pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

Write-Host "✅ Virtual environment setup complete!" -ForegroundColor Green
Write-Host "To activate: .\venv_ai_email\Scripts\Activate.ps1" -ForegroundColor Yellow
Write-Host "To start server: python main.py" -ForegroundColor Yellow