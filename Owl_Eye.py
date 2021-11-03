#add modules
from colorama import Fore, Back, Style
import pyfiglet
import requests
from bs4 import BeautifulSoup
import time

#print banner

banner =  """                                                                                
                                                                                
                         #                                                      
                        @.                                                      
                       &@  *                                                    
                       @&  ,@@@@@@@@@@@@@@@/.                                   
                      (@@    &@@@@@@@@@@@%*@@@@@@@.                             
                 @@&&&@@@%     *@@@@@@@@( ,@@@@@@@@@@@.                         
                                  .@@*&@%  & .@@@@@@@@@@@                       
                              ,       .@,*@&  @@@@@@@@@@@@@                     
                                @.          &@,@@@@@@@@@@@@@@                   
                               %@@@@*         @@@@@@@@@@@@@@@@/                 
                             &@ ,.,@@@@,       /@@@@@@@@@@@@@@@#                
                            @   #@@@@#(@@/      /%@@@@@@@@@@@@@@,               
                           %   #@@@.,,**#@@      @ @@@@@@@@@@@@@@               
                               %@@/.***/ .@@..   * /*@@@@@@@@@@@@,              
                               &@@# ,**/(%%&@&      .#@@@@@@@@@@@(              
                            ,  .@@@&.,****(#@@#     *&*@@@@@@@@@@/              
                             #.  @&@@@&*..(#@@%      @@@@@@@@@@@@.              
                               @.  &.#@@@@@@@@@,. . .&@@@@@@@@@@@               
                                  %%        *@&@@@@@@@@@@@@@@@@@                
                                                  @@@@@@@@@@@@@               
                                                   (@@@@@@@@@&                  
                                          **        @@@@@@@@                    
                                       #&@@* ./    #@@@@@@                      
                                     #.@@@@@@@@  .@@@@@(                        
                                   . @@@@@@@@%@@@@@@,                           
                                 @*@@ @@@@@@@@@*                                
                               .@@"""

result = pyfiglet.figlet_format("               O w l  E y e")
print(Fore.GREEN + banner)
time.sleep(3)
print(Fore.RED + result)

#add sign & version
time.sleep(3)
print(Fore.YELLOW + "         [+]Coded By Black Owl[+]")
time.sleep(3)
print(Fore.YELLOW + "         [+]V0.1[+]\n\n")

#check network connection
try:
	requests.get("https://www.google.com/")
except:
	print(Fore.RED + "[+]No internet connection.... connect to internet & try again...")

#get input url/ip
get_ip = input("Enter Web site URL or Ip address :- ")

#requests to url/ip
page = requests.get(f"https://who.is/whois/{get_ip}")

soup = BeautifulSoup(page.text, "html.parser")

#get topics using functio
def topic_num(topic):
	main_topic1 = soup.find_all("span", class_="lead")[topic]
	print(Fore.CYAN + f"~~{main_topic1.text}~~\n\n")

#get data using function
def inde_num(num):
        get_class = soup.find_all("div", class_="col-md-4 queryResponseBodyKey")[num]
        get_class1 = soup.find_all("div", class_="col-md-8 queryResponseBodyValue")[num]
        print(Fore.YELLOW + f">>{get_class.text} = {get_class1.text}\n")

#call to functions by order
#get topic 1
topic_num(0)

#get data for topic 1
inde_num(0)
inde_num(1)
inde_num(2)
inde_num(3)

#get dates
topic_num(1)

#get data from dates
inde_num(4)
inde_num(5)
inde_num(6)

#get name servers
time.sleep(3)
topic_num(2)

#get data from name servers
def server_num(num1):
        get_class = soup.find_all("div", class_="row")[num1]
        print(get_class.text)
server_num(20)

#get simillara domain
time.sleep(3)
topic_num(3)

#get data for similar domain
similar = soup.find_all("div", "col-md-12 queryResponseBodyValue")[0]
print(similar.text)

#get owner topic
time.sleep(3)
topic_num(4)

#try to get owner info
try:
	def owner_topic(owner_div):
		owner = soup.find_all("div", class_="col-md-offset-1 col-md-4")[owner_div]
		owner_data = soup.find_all("div", class_="col-md-7")[owner_div]
		print(Fore.BLUE + f">>{owner.text} = {owner_data.text}")


  #call to function
	owner_topic(0)
	owner_topic(1)
	owner_topic(2)
	owner_topic(3)
	owner_topic(4)
	owner_topic(5)
	owner_topic(6)
	owner_topic(7)
	owner_topic(8)

	#administrator contact information
	print("Administrative Contact Information:\n")
	owner_topic(9)
	owner_topic(10)
	owner_topic(11)
	owner_topic(12)
	owner_topic(13)
	owner_topic(14)
	owner_topic(15)
	owner_topic(16)
	owner_topic(17)

	#Technical Contact Information
	print("Technical Contact Information:\n")
	owner_topic(18)
	owner_topic(19)
	owner_topic(20)
	owner_topic(21)
	owner_topic(22)
	owner_topic(23)
	owner_topic(24)
	owner_topic(25)
	owner_topic(26)

except:
	print(Fore.RED + "Whois information for this domain has been blocked....!")
