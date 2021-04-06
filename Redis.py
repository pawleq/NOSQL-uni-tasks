import redis
player = redis.Redis(host='localhost', port=6379, db=0)

player_id = 0
character_id = 1000
stash = 100

def operations():
    print ("Greetings, what task do you want to execute? :"
            "\n To register a new account? Press 1"
            "\n To create a character for an existing account? Press 2"
            "\n To make a transaction beetwen characters? Press 3"
            "\n Clear DB. Press 4"
            "\n To exit press 5")

    choice = input()
    return int(choice)
    
def register():
    username = input("Enter the account username : ")
    if username in player:
        username = input("Username in use. Try again.")
    password = input("Ender the desired password : ")
    account = {'username': username, 'password': password}
    player.hmset(player_id, account)
    print ("Your unique player id is " + str(player_id))

def character():
    id = int(input("Enter player ID : "))
    while id > player_id :
        id = int(input("Active player with this id, was not found. Try again"))
    nickname = input("Enter nickname for character : ")
    character = {'nickname': nickname,'player': id,'stash': stash}
    player.hmset(str(character_id), character)

def payment():
    paying_char = input("Who will transfer the gold?: ")
    receiving_char = input("Who will receive the gold? : ")
    amount = int(input("How much gold should be transfered? : "))
    p = player.pipeline()
    p.watch(paying_char, receiving_char)
    if amount <= int(player.hget(paying_char, 'stash')):
        consists = p.exists(paying_char, receiving_char)
        if consists :
            p.multi()
            p.hincrby(receiving_char, 'stash', amount)
            p.hincrby(paying_char, 'stash', -amount)
            p.execute()
            print('Trade was sucessful')
            print('Current stash of '+str(paying_char)+' is '+str(player.hget(paying_char, 'stash')))
            print('Current stash of '+str(receiving_char)+' is '+str(player.hget(receiving_char, 'stash')))
        else :
            p.unwatch(paying_char, receiving_char)
    else :
        print ("You cannot go to a dept.")
        
while True:
    choice = operations()
    if choice in range (1,6):
        if choice == 5 :
            break
        if choice == 1 :
            register()
            player_id += 1
        if choice == 2 :
            character()
            character_id +=1
        if choice == 3 :
            payment()
        if choice == 4 :
            player.flushdb()