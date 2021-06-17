print('''
                         _
                           ,--.\`-. __
                         _,.`. \:/,"  `-._
                     ,-*" _,.-;-*`-.+"*._ )
                    ( ,."* ,-" / `.  \.  `.
                   ,"   ,;"  ,"\../\  \:   \
                  (   ,"/   / \.,' :   ))  /
                   \  |/   / \.,'  /  // ,'
                    \_)\ ,' \.,'  (  / )/
                        `  \._,'   `"
                           \../
                           \../
                 ~        ~\../           ~~
          ~~          ~~   \../   ~~   ~      ~~
     ~~    ~   ~~  __...---\../-...__ ~~~     ~~
       ~~~~  ~_,--'        \../      `--.__ ~~    ~~
   ~~~  __,--'              `"             `--.__   ~~~
~~  ,--'                                         `--.
   '------......______             ______......------` ~~
 ~~~   ~    ~~      ~ `````---"""""  ~~   ~     ~~
        ~~~~    ~~  ~~~~       ~~~~~~  ~ ~~   ~~ ~~~  ~
     ~~   ~   ~~~     ~~~ ~         ~~       ~~   SSt
              ~        ~~       ~~~       ~
''')
print("Welcome to Roberto's Treasure Island.")
print("Your mission is to find the treasure.")
name = input("Enter your name: ")
direction = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()
if direction == "right":
    print("You fell through a hole...Game Over.")
elif direction == "left":
    choice = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()
    if choice == "swim":
        print("You got eaten by 10 aligators...Game Over.")
    else:
        door = input('You\'ve arrive at the island unharmed. There is a house with 3 doors. Which door? One red, one yellow and one blue. Which color do you choose?\n').lower()
        if door == "red":
            print("The room is up in flames...Game Over.")
        elif door == "blue":
            print("You drowned..That was the door to the ocean...Game Over.")
        elif door == "yellow":
            
            print(name + " You opened the Victory Door! You Win!")

    

 







