# DNS PRACTICE
## Prompt
1. Please create a new github repo called 'DNS practice' 

2. Inside the repo, please create a simple flask app (can be your PssP or something else, I have no preference) - this flask app should then be deployed on a VM in either GCP or Azure 

3. Register a domain name using .TECH (be sure to have your github student account linked so it is FREE) - or if you have already purchased domains in the past and use something like godaddy, that is also fine [https://get.tech/github-student-developer-pack] 

4. Create a A record that links together the domain with the IP address of your flask app deployed on either GCP or Azure 

5. Create a markdown/readme file that contains the following information: 
The name of your purchased domain 
A copy of the 'A' record settings that you needed to write (name, value, TTL) 
The cloud vendor you selected 
Brief instructions if something were to want to re-recreate your app on their own cloud VM 
6. A "/photos" folder that contains screen shots of your live flask application deployed on your website 

7. Once completed, please feel free to shut down the instance/VM to save money - UNLESS you want to keep it live (e.g., maybe your are creating a personal CV website to show off your new skills....)

## DNS 'A' Record Settings:
- ***Name***: @.zincare.tech
- ***Destination IPV4 Address***: 34.27.70.241
- ***TTL***: 7200

## Cloud Vendor Used
GCP

## Stepts to Recreate:
  1. Create VM with appropriate settings
  2. Copy the external IP address of the VM
  3. Go into DNS management settings and paste IP address into the 'A' record settings
  4. SSH into VM and run the following code:
  
       - sudo apt-get update
      
       - sudo apt install python3-pip
       
       - pip3 install flask
       
       - sudo apt install python3-flask
       
       - git clone the repository containing flask app
       
       - cd into that repository
       
       - run python3 "insert flask app filename here"
