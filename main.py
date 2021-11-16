# importing the requests library
import requests

failure = False

# set the value below to either GET or POST
cmd_choice = input("Enter g to GET or p to POST: ")
if cmd_choice=='g':
  print("You have chosen to make a GET request.")
elif cmd_choice=='p':
  print("You have chosen to mane a POST request.")
else:
  print("Invalid choice")
  failure = True
print("")

if failure==False:
  # set the URL for the command you would like to 
  print("Complete this URL to make your request.")
  URL = input("https://cs-api.pltw.org/")
  URL = "https://cs-api.pltw.org/" + URL

  print("\nShould I send the following request:")
  if cmd_choice == "g":
    print("GET  " + URL)
  else:
    print("POST  " + URL)
  choice = input("Y or N? ")
  
  if (choice=="Y") or (choice=='y'):
    if cmd_choice=="g":
      p = requests.get( url = URL )
      # printing the output
      print(p.text)
    else:
      p = requests.post( url = URL )
      # printing the output
      print("\n\n\nResults of the request:\n")
      print(p.text)
  else:
    print("Request canceled")    

