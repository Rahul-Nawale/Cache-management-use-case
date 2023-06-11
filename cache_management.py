# Full Name : Rahul Nawale
# Student ID - 201669264

def fifo(requests, cache):
    for i in requests:
        if i not in cache:
            print("miss")
            if len(cache) < 8:
                cache.append(i)
            else:
                del cache[0]
                cache.append(i)
        else:
            print("hit")
    print(cache)
    cache = []

def lfu(requests, cache):
    dict = {}
    for i in requests:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] = dict[i] + 1
        if i not in cache:
            print("miss")
            if len(cache) < 8:
                cache.append(i)
            else:
                minval = min(dict.values())
                res = [k for k, v in dict.items() if v == minval]
                pop = sorted(res)[0]
                cache.remove(pop)
                cache.append(i)
        else:
            print("hit")
    print(cache)
    cache = []





def userinput():
    requests = []
    cache = []
    try:
        while True:
            requests.append(int(input("Enter the page number :")))
            if requests[-1] == 0:
                del requests[-1]
                break
    # if the input is not-integer, just print the list
    except:
        exit("Invalid input")

    response = ""
    response = input("Enter 1, 2 or Q: ")
    if response == "Q":
        exit()
    elif response == "1":
        fifo(requests, cache)
    elif response == "2":
        lfu(requests,cache)
    else:
        exit("Invalid input")
    return userinput()



userinput()