
#!/bin/bash
sudo apt-get update
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
sudo pip3 install virtualenv


mkdir django
cd django

virtualenv myprojectenv
# git clone the repo
git clone "https://gitlab.crio.do/COHORT_ME_BUILDOUT_XMEME_ENROLL_1612436694845/muthukumaranmblaze99-me_buildout_xmeme.git"
# cd to the cloned repo directory
source myprojectenv/bin/activate

cd muthukumaranmblaze99-me_buildout_xmeme

# Run the user’s installation steps which will install any necessary dependencies required for the server to run, with sudo permission



chmod +x install.sh

sudo ./install.sh


# 1. Run the user’s server execution steps which will bring up the server

# 2. We’ll be running your server_run.sh as a background process (using &) so that we can run the next set of commands

chmod +x server_run.sh

./server_run.sh &


# 3. Add a sleep timer to sleep.sh depending upon how long you want to sleep so that the server is ready.

chmod +x sleep.sh

./sleep.sh


# Execute the GET /memes endpoint using curl to ensure your DB is in a clean slate

# Should return an empty array.

curl --location --request GET 'http://0.0.0.0:8081/memes'


# Execute the POST /memes endpoint using curl



curl --location --request POST 'http://0.0.0.0:8081/memes/' \
--header 'Content-Type: application/json' \
--data-raw '{ 
        "name": "Muthu-postman22",
        "url": "https://imgur.com/gallery/sZPbqny",
        "caption": "i finished post(updated)"
    }'

# Execute the GET /memes endpoint using curl

curl --location --request GET 'http://0.0.0.0:8081/memes/'


# If you have swagger enabled, make sure it is exposed at localhost:8080

curl --location --request GET 'http://0.0.0.0:8081/swagger-ui/'

