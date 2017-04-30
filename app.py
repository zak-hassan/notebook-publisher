from __future__ import print_function
import os
from flask import Flask
import sys
from random import random
from operator import add

 

app = Flask(__name__)

@app.route("/")
def hello():
    
    # coding: utf-8
    
    # In[1]:
    
    print("Testing 1 2 3 4 5...")
    
    
    # In[ ]:
    
    
    

    return "Testing 1 2 3 4 5..."


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
