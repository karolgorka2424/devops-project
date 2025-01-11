# 1. Build the Docker image
docker build -t my-flask-app .

# 2. Run the container
docker run -p 5000:5000 my-flask-app

Once running, you can test the endpoints:

-Visit http://localhost:5000/ to see "Hello World"
-Visit http://localhost:5000/hello/YourName to see "Hello YourName"

If running in GitHub CodeSpaces:

-Visit [https://yourname-yourproject-xxxx.preview.app.github.dev] to see "Hello World"
-Visit [https://yourname-yourproject-xxxx.preview.app.github.dev/hello/]YourName to see "Hello YourName"

Change project name and your name accordingly