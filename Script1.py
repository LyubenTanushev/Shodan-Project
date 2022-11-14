import shodan
shodan_key = "o1AbCpf0RBvM67oXguIx1IuOql5lTQum"

api = shodan.Shodan(shodan_key)

def myOut(received):
    f=open("output.txt", "a+")
    f.write(received)
    f.write("\n")
    f.close()

item = input("input seach query\n")
myFind = []
try:
    results = api.search(item)
    print("total matches = {}".format(results['total']))
    for result in results['mmatches']:
        myFind.append(str(result['ip_str'])+" "+str(result['hostnames'])+" "+str(result['os']))

except:
    print("error")

output=int(input("print to screen [1] or save to file [2]\n"))
if output==1:
    for val in myFind:
        print(val)
elif output==2:
    for val in myFind:
        myOut(val)
else:
    print("input wrong number")