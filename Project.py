
MI= [
{"jn":45,"pname":"Rohit Sharma","runs":6211,"wickets":15,"tname":"Mumbai_Indians"},
{"jn":63,"pname":"Suryakumar Yadav","runs":3249,"wickets":0,"tname":"Mumbai_Indians"},
{"jn":99,"pname":"Ishan Kishan","runs":2324,"wickets":0,"tname":"Mumbai_Indians"},
{"jn":77,"pname":"Tilak Varma","runs":1200,"wickets":0,"tname":"Mumbai_Indians"},
{"jn":33,"pname":"Hardik Pandya","runs":2309,"wickets":53,"tname":"Mumbai_Indians"},
{"jn":19,"pname":"Tim David","runs":659,"wickets":0,"tname":"Mumbai_Indians"},
{"jn":25,"pname":"Romario Shepherd","runs":150,"wickets":12,"tname":"Mumbai_Indians"},
{"jn":93,"pname":"Jasprit Bumrah","runs":70,"wickets":145,"tname":"Mumbai_Indians"},
{"jn":74,"pname":"Piyush Chawla","runs":584,"wickets":179,"tname":"Mumbai_Indians"},
{"jn":36,"pname":"Gerald Coetzee","runs":100,"wickets":18,"tname":"Mumbai_Indians"},
{"jn":31,"pname":"Akash Madhwal","runs":20,"wickets":19,"tname":"Mumbai_Indians"}
]

CSK = [
{"jn":7,"pname":"MS Dhoni","runs":5082,"wickets":0,"tname":"Chennai_Super_Kings"},
{"jn":8,"pname":"Ravindra Jadeja","runs":2692,"wickets":152,"tname":"Chennai_Super_Kings"},
{"jn":25,"pname":"Shivam Dube","runs":1100,"wickets":4,"tname":"Chennai_Super_Kings"},
{"jn":31,"pname":"Ruturaj Gaikwad","runs":2380,"wickets":0,"tname":"Chennai_Super_Kings"},
{"jn":10,"pname":"Ajinkya Rahane","runs":4642,"wickets":1,"tname":"Chennai_Super_Kings"},
{"jn":88,"pname":"Moeen Ali","runs":1162,"wickets":35,"tname":"Chennai_Super_Kings"},
{"jn":18,"pname":"Deepak Chahar","runs":90,"wickets":72,"tname":"Chennai_Super_Kings"},
{"jn":90,"pname":"Matheesha Pathirana","runs":20,"wickets":34,"tname":"Chennai_Super_Kings"},
{"jn":47,"pname":"Tushar Deshpande","runs":15,"wickets":42,"tname":"Chennai_Super_Kings"},
{"jn":54,"pname":"Maheesh Theekshana","runs":40,"wickets":30,"tname":"Chennai_Super_Kings"},
{"jn":22,"pname":"Mitchell Santner","runs":200,"wickets":20,"tname":"Chennai_Super_Kings"}
]

RCB = [
{"Jersey NO":18,"pname":"Virat Kohli","runs":8004,"wickets":4,"tname":"Royal Challengers Bangalore"},
{"Jersey NO":97,"pname":"Faf du Plessis","runs":4571,"wickets":0,"tname":"Royal Challengers Bangalore"},
{"Jersey NO":32,"pname":"Glenn Maxwell","runs":2719,"wickets":35,"tname":"Royal Challengers Bangalore"},
{"Jersey NO":21,"pname":"Rajat Patidar","runs":799,"wickets":0,"tname":"Royal Challengers Bangalore"},
{"Jersey NO":19,"pname":"Mohammed Siraj","runs":56,"wickets":78,"tname":"Royal Challengers Bangalore"},
{"Jersey NO":7,"pname":"Dinesh Karthik","runs":4516,"wickets":0,"tname":"Royal Challengers Bangalore"},
{"Jersey NO":9,"pname":"Josh Hazlewood","runs":30,"wickets":52,"tname":"Royal Challengers Bangalore"},
{"Jersey NO":5,"pname":"Mahipal Lomror","runs":350,"wickets":2,"tname":"Royal Challengers Bangalore"},
{"Jersey NO":13,"pname":"Will Jacks","runs":230,"wickets":5,"tname":"Royal Challengers Bangalore"},
{"Jersey NO":24,"pname":"Reece Topley","runs":15,"wickets":12,"tname":"Royal Challengers Bangalore"}
]

GT = [
{"Jersey NO":77,"pname":"Shubman Gill","runs":3216,"wickets":0,"tname":"Gujarat Titans"},
{"Jersey NO":63,"pname":"Jos Buttler","runs":3582,"wickets":0,"tname":"Gujarat Titans"},
{"Jersey NO":50,"pname":"Sherfane Rutherford","runs":1065,"wickets":3,"tname":"Gujarat Titans"},
{"Jersey NO":5,"pname":"Washington Sundar","runs":378,"wickets":37,"tname":"Gujarat Titans"},
{"Jersey NO":99,"pname":"Sai Kishore","runs":50,"wickets":22,"tname":"Gujarat Titans"},
{"Jersey NO":66,"pname":"Sai Sudharsan","runs":1034,"wickets":0,"tname":"Gujarat Titans"},
{"Jersey NO":12,"pname":"Shahrukh Khan","runs":426,"wickets":0,"tname":"Gujarat Titans"},
{"Jersey NO":25,"pname":"Kagiso Rabada","runs":200,"wickets":117,"tname":"Gujarat Titans"},
{"Jersey NO":13,"pname":"Mohammed Siraj","runs":56,"wickets":78,"tname":"Gujarat Titans"},
{"Jersey NO":24,"pname":"Prasidh Krishna","runs":10,"wickets":49,"tname":"Gujarat Titans"},
{"Jersey NO":19,"pname":"Rashid Khan","runs":450,"wickets":149,"tname":"Gujarat Titans"}
]

IPL_DB={"MI":MI,"CSK":CSK,"RCB":RCB,"GT":GT}
print("Display player pname who scores more than 5000 runs: ")
for team in IPL_DB.values():
    for player in team:
        if  player["runs"] >= 5000:
            print(player["pname"], "-", player["runs"])
print("--"*20)
            
print("Display player pname who takes wickets more than 20 : ")
for team in IPL_DB.values():
    for player in team:
        if  player["wickets"] >= 50:
            print(player["pname"], "-", player["wickets"])
print("--"*20)

print("Display player pname who scores more than 5000 runs: ")
for team in IPL_DB.values():
    for player in team:
        if  player["runs"] >= 5000:
            print(player["pname"], "-", player["runs"])
print("--"*20)

for team in IPL_DB.values():
    for player in team:
        if player["runs"]>=2000 and player["wickets"]>=20:
            print(player["pname"],"- runs:",player["runs"]," - ","wickets: ",player["wickets"])
print("--"*20)

for team in IPL_DB.values():
    for player in team:
        if player["runs"]<=1500 and player["wickets"]<=20:
            print(player["pname"],"- runs:",player["runs"]," - ","wickets: ",player["wickets"],"\t\t",player["tname"])
print("--"*40)

top_runs=0
top_runner=""
for team,players in IPL_DB.items():
    for player in players:
        if player["runs"]>top_runs:
            top_runs=player["runs"]
            top_runner=player["pname"]
print("Top Runner is ",top_runner," and his total runs is ",top_runs)
print("--"*40)

max_wickets=0
Player=""
for players in IPL_DB.values():
    for player in players:
        if player["wickets"]>max_wickets:
            max_wickets=player["wickets"]
            Player=player["pname"]
print("The top wicket Taker is ",Player," and he takes ",max_wickets," wickets in IPL")