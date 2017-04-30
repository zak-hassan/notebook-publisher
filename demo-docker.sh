

# Run the publisher to convert the python into python flask app
python3 publisher.py notebooks/Test1.ipynb
# Run Docker build
./build-docker.sh
# Start up docker container
./run-docker.sh
