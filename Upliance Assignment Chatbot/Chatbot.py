import random

game_state={"round":1,"user_score":0,"bot_score":0,"user_bomb":False,"bot_bomb":False,"game_over":False}

Valid_moves=["rock","paper","scissors","bomb"]

def validate_move(move, bomb_used):
    move=move.lower().strip()
    if move not in Valid_moves:
        return{"is_valid":False, "reason":"Invalid Move"}
    if move=="bomb" and bomb_used:
        return{"is_valid":False, "reason":"Bomb is already used"}
    return{"is_valid":True,"reason":"Valid Move"}

def resolve_round(user_move, bot_move):
    if user_move==bot_move:
        return "draw"
    if user_move=="bomb" and bot_move != "bomb":
        return "user"
    if bot_move=="bomb" and user_move!="bomb":
        return "bot"
    rules={
        "rock":"scissors",
        "scissors":"paper",
        "paper":"rock"
    }
    if rules.get(user_move)==bot_move:
        return "user"
    else:
        return "bot"
    
def update_state(result,user_move,bot_move):
    if user_move=="bomb":
        game_state["user_bomb"]=True
    if bot_move=="bomb":
        game_state["bot_bomb"]=True
    if result=="user":
        game_state["user_score"]+=1
    elif result =="bot":
        game_state["bot_score"]+=1
    game_state["round"] +=1
    if game_state["round"]>3:
        game_state["game_over"]=True

def explain_rules():
    print("Game Rules:")
    print("• Best of 3 rounds")
    print("• Moves: rock, paper, scissors, bomb")
    print("• Bomb beats everything but can be used once")
    print("• Invalid move wastes the round")
    print("• Game ends automatically after 3 rounds\n")


def bot_choose_move():
    moves=["rock","paper","scissors"]
    if not game_state["bot_bomb"]:
        moves.append("bomb")
    return random.choice(moves)

def play():
    print(f"\nRound {game_state['round']} of 3")
    user_input=input("Enter your move: ").lower()

    validation=validate_move(user_input,game_state["user_bomb"])
    bot_move=bot_choose_move()

    if not validation["is_valid"]:
        print(f"Invalid move: {validation['reason']}")
        print("Round is Wasted")
        game_state["round"]+=1
        if game_state["round"]>3:
            game_state["game_over"]=True
        return
    result =resolve_round(user_input,bot_move)
    update_state(result,user_input,bot_move)
    print(f"You Played : {user_input}")
    print(f"Bot Played: {bot_move}")

    if result=="draw":
        print("Result : Draw")
    elif result=="user":
        print("Result : You win this round")
    else:
        print("Result : Bot win this round")

    print (f"Score \n You: {game_state['user_score']} \nBot: {game_state['bot_score']}")

def end_game():
    print("\nGame Over")
    if game_state["user_score"]>game_state["bot_score"]:
        print("Final Result: You Won the game")
    elif game_state["bot_score"]>game_state["user_score"]:
        print("Final Result : Bot won the game")
    else:
        print("Final Result : Draw")



def main():
    explain_rules()

    while not game_state["game_over"]:
        play()

    end_game()


if __name__ =="__main__":
    main()

