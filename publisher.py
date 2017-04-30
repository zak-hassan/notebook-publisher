import argparse
import os

def main():
    " Application entry point "
    parser = argparse.ArgumentParser()
    parser.add_argument("notebook", help="path to notebook to be converted")
    args = parser.parse_args()
    pa= parser.parse_args()
    print(args.notebook)
    # Converting python notebook to a python script
    os.system("ipython nbconvert --to script {fname} ".format(fname=args.notebook))

    filename="{fname}".format(fname=args.notebook.replace("ipynb","py"))
    with open(filename) as f:
        content = f.readlines()
        codeblock='    '.join(content)
        for i, j in enumerate(content):
            if j.startswith("print"):
                rtn=content[i].replace("print","return")
                print(rtn)



        with open("app.py", "w") as w:
            flask="""\
from __future__ import print_function
import os
from flask import Flask
import sys
from random import random
from operator import add

 

app = Flask(__name__)

@app.route("/")
def hello():
    {msg}
    {rtn}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
""".format(msg=codeblock, rtn=rtn)
            w.write(flask)
            # Create docker file then push it to docker hub

            # Create openshift-template to deploy this service.




if __name__ == '__main__':
    main()