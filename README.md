1. Build the Docker image
docker build -t my-flask-app .

2. Run the container
docker run -p 5000:5000 my-flask-app

Once running, you can test the endpoints:

-Visit http://localhost:5000/ to see "Hello World"
-Visit http://localhost:5000/hello/YourName to see "Hello YourName"

If running in GitHub CodeSpaces:

-Visit [https://yourname-yourproject-xxxx.preview.app.github.dev] to see "Hello World"
-Visit [https://yourname-yourproject-xxxx.preview.app.github.dev/hello/]YourName to see "Hello YourName"

Change project name and your name accordingly.

If Trivy is not installed after push or pull action on the main branch:

sudo apt-get update
sudo apt-get install -y wget apt-transport-https gnupg lsb-release
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update
sudo apt-get install -y trivy

You can use Trivy manually by:

trivy image my-flask-app
