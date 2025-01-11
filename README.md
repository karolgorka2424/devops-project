## Quick Start

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

### Docker Deployment

1. Build the Docker image:
```bash
docker build -t my-flask-app .
```

2. Run the container:
```bash
docker run -p 5000:5000 my-flask-app
```

## Accessing the Application

### Local Environment
- Homepage: http://localhost:5000/
- Custom greeting: http://localhost:5000/hello/YourName

### GitHub Codespaces
- Homepage: https://yourname-yourproject-xxxx.preview.app.github.dev/
- Custom greeting: https://yourname-yourproject-xxxx.preview.app.github.dev/hello/YourName

Replace `yourname-yourproject-xxxx` with your actual Codespace URL.

## Security Scanning with Trivy

Trivy vulnerability scanner is automatically triggered on:
- Pull requests to the main branch
- Push events to the main branch

### Manual Trivy Scan

If Trivy is not installed, run:
```bash
sudo apt-get update
sudo apt-get install -y wget apt-transport-https gnupg lsb-release
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update
sudo apt-get install -y trivy
```

To scan your Docker image:
```bash
trivy image my-flask-app
```

## Project Structure
```
.
├── .github
│   └── workflows
│       └── ci.yml     # GitHub Actions workflow
├── .gitignore         # Git ignore rules
├── Dockerfile         # Docker configuration
├── README.md          # Project documentation
├── main.py           # Flask application
└── requirements.txt   # Python dependencies
```

## CI/CD Pipeline

The project includes a GitHub Actions workflow that:
1. Builds the Docker image
2. Runs automated tests
3. Performs security scanning with Trivy
4. Executes additional checks on main branch merges

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request