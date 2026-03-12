'''level 1'''
movie = {}

movie["Chhava"] = ["Vicky Kaushal", "Rashmika Mandanna", "Akshaye Khanna"]
movie["Fighter"] = ["Hrithik Roshan", "Deepika Padukone", "Anil Kapoor"]
movie["Pushpa 2"] = ["Allu Arjun", "Rashmika Mandanna", "Fahadh Faasil"]
movie["Kalki 2898 AD"] = ["Prabhas", "Deepika Padukone", "Amitabh Bachchan"]
movie["Dhurandhar"] = ["Akshaye Khanna", "Ranveer Singh", "Sanjay Dutt", "R. Madhavan"]
movie["Singham Again"] = ["Ajay Devgn", "Kareena Kapoor", "Akshay Kumar"]

print(movie)
print("--"*20)

print("Keys() Method : ")
print(movie.keys())
print("--"*20)

print("Values() Method : ")
print(movie.values())
print("--"*20)

print("Items() Method   Way 1 => directly in print statment: ")
print(movie.items())
print("--"*20)

print("Way 2 => using for loop :")
for i in movie.items():
    print(i)
print("--"*20)

print("display keys using items method :")
for i,j in movie.items():
    print(i)
print("--"*20)

print("display values using items method : ")
for i,j in movie.items():
    print(j)
print("--"*20)

print(" Count of the Akshya Khanna present in movies")
count=0
for i in movie.values():
    for j in i:
        if j=="Akshaye Khanna":
            count=count+1    
print(count)    
print("--"*20)   

print("display first actor name from dhurander movie ")
print(movie.get("Dhurandhar")[0])
print("--"*20)

for a in movie["Dhurandhar"]:
    print(a)
    break
print("--"*20)

print(movie["Dhurandhar"][0][8:])
print("--"*20)

fa=movie["Dhurandhar"]
print(fa[0][::-1])
print("--"*20)

fa=movie["Dhurandhar"]
print(fa[0][5])
print("---"*15)

print("display names oa all actor and actress on console one by one")
for m,a in movie.items():
    print(m,"--->")
    for a in a:
        print("          ",a,"--->")
        for i in a.split():
            print(3*"\t",i)
            for j in i:
                print(4*"\t",j)        
    print("---"*15)