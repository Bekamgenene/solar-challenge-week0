# Solar Challenge Week 0

## Environment Setup

### Prerequisites
- Python 3.11 or higher
- Git

### Installation

1. **Clone the repository**
   \`\`\`bash
   git clone https://github.com/Bekamgenene/solar-challenge-week0.git
   cd solar-challenge-week0
   \`\`\`

2. **Set up virtual environment**
   \`\`\`bash
   python -m venv myenv
   
   # Activate on Windows:
   myenv\\Scripts\\activate
   
   # Activate on macOS/Linux:
   source myenv/bin/activate
   \`\`\`

3. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Verify installation**
   \`\`\`bash
   python -c "import pandas; print('Setup successful!')"
   \`\`\`

### Project Structure
\`\`\`
solar-challenge-week0/
├── .github/workflows/  # CI/CD configurations
├── data/               # Data files (gitignored)
├── notebooks/          # Jupyter notebooks
├── src/                # Source code
├── tests/              # Test files
└── scripts/            # Utility scripts
\`\`\`

### Development
- Use \`setup-task\` branch for development
- Create pull requests to merge into \`main\`
- CI automatically runs on push to verify dependencies
