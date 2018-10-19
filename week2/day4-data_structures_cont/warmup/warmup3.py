my_set = {2, 3, 5}
my_fav_primes = {11, 13, 7}
my_tot_primes = my_set.union(my_fav_primes)
newprime = int(input("New Prime to add: "))
primestatus = "prime"
for num in range(2,newprime):
    if newprime % num == 0:
        primestatus = "not prime"
        break
if primestatus == "prime":
    my_tot_primes.add(newprime)
else:
    print("Not a prime!")
print(my_tot_primes)
