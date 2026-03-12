MI=["Rohit Sharma","Ryan Rickelton","Tilak Varma","Suryakumar Yadav","Hardik Pandya","Naman Dhir",
     "Will Jacks","Mitchell Santner","Trent Boult","Deepak Chahar","Jasprit Bumrah"]

RCB=["Virat Kohli","Phil Salt","Jitesh Sharma","Rajat Patidar","Devdutt Padikkal","Krunal Pandya",
     "Tim David", "Romario Shepherd","Josh Hazlewood","Suyash Sharma","Bhuvneshwar Kumar"]

GT=["Shubman Gill","Jos Buttler","Sherfane Rutherford","Washington Sundar","Sai Kishore","Sai Sudharsan",
    "Shahrukh Khan","Kagiso Rabada","Mohammed Siraj","Prasidh Krishna","Rashid Khan"]

CSK=["Ruturaj Gaikwad","MS Dhoni","Devon Conway","Rahul Tripathi","Rachin Ravindra","Ravichandran Ashwin",
    "Sam Curran","Ravindra Jadeja","Shivam Dube","Noor Ahmad","Khaleel Ahmed"]

DC=["KL Rahul","Abishek Porel","Tristan Stubbs","Jake Fraser-McGurk","Karun Nair","Faf du Plessis"
    "Ashutosh Sharma","Vipraj Nigam","Axar Patel","Mitchell Starc","Kuldeep Yadav"]

LSG=["Rishabh Pant","Nicholas Pooran","David Miller","Aiden Markram","Mitchell Marsh","Abdul Samad",
     "Shahbaz Ahamad","Ayush Badoni","Avesh Khan","Akash Deep","Ravi Bishnoi"]

RR=["Sanju Samson","Dhruv Jurel","Vaibhav Suryavanshi","Shimron Hetmyer","Yashasvi Jaiswal","Riyan Parag",
    "Nitish Rana","Jofra Archer","Maheesh Theekshana","Wanindu Hasaranga","Akash Madhwal"]

SRH=["Pat Cummins","Ishan Kishan","Heinrich Klaasen","Travis Head","Abhinav Manohar","Harshal Patel",
     "Abhishek Sharma","Nitish Kumar Reddy","Mohammad Shami","Rahul Chahar","Eshan Malinga"]

KKR=["Venkatesh Iyer","Quinton de Kock","Rahmanullah Gurbaz","Rinku Singh","Angkrish Raghuvanshi","Ajinkya Rahane",
     "Moeen Ali","Andre Russell","Anrich Nortje","Harshit Rana","Sunil Narine"]

PBKS=["Shreyas Iyer","Josh Inglis","Prabhsimran Singh","Nehal Wadhera","Shashank Singh","Marcus Stoinis",
      "Glenn Maxwell","Marco Jansen","Priyansh Arya","Arshdeep Singh","Yuzvendra Chahal"]


# any letter find in the case for capital or small
letter = input("Enter a letter to search: ").lower()
teams = [MI, RCB, GT, CSK, DC, LSG, RR, SRH, KKR, PBKS]
for team in teams:
    for player in team:
        if letter in player.lower():
            print(player)
print("--"*20)

# Searching on the first letter in the string 
print("Name startwith letter R : ")
for i in MI:
    if i.startswith("R"):
        print(i)
print("--"*20)

# Search the letters in middle or any position
print("Player name where J is present :")
for i in CSK:
    if "j" in i:
        print(i)
print("--"*20)