

# Run the publisher to convert the python into python flask app
python publisher.py notebooks/PiSpark.ipynb
# Run Docker build
./build-docker.sh
# Start up docker container
./run-docker.sh
