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
    game_state["round"]+=1
    if game_state["round"]>3:
        game_state["game_over"]=True

def bot_choose_move():
    moves=["rock","paper","scissors"]
    if not game_state["bot_bomb"]:
        moves.append("bomb")
    return random.choice(moves)

class RefereeAgent:

    def explain_rules(self):
        return ("Game Rules:\n"
        "• Best of 3 rounds\n"
        "• Moves: rock, paper, scissors, bomb\n"
        "• Bomb beats everything but can be used once\n"
        "• Invalid move wastes the round\n"
        "• Game ends automatically after 3 rounds\n"
        )

    def respond(self,user_input: str) -> str:
        user_input=user_input.lower()
        user_move=None
        for move in Valid_moves:
            if move in user_input:
                user_move=move
                break

        if user_move is None:
            validation={"is_valid":False,"reason":"Could not understand your move"}
        else:
            validation=validate_move(user_move,game_state["user_bomb"])

        if not validation["is_valid"]:
            game_state["round"]+=1
            if game_state["round"]>3:
                game_state["game_over"]=True
            return f"Invalid move: {validation['reason']}.This Round is Wasted."

        bot_move=bot_choose_move()
        result=resolve_round(user_move,bot_move)
        update_state(result,user_move,bot_move)
        response=(
            f"Round {game_state['round']-1} of 3\n"
            f"You Played: {user_move}\n"
            f"Bot Played: {bot_move}\n"
        )

        if result=="draw":
            response+="Result: Draw\n"
        elif result=="user":
            response+="Result: You win this round\n"
        else:
            response+="Result: Bot wins this round\n"

        response+=f"Score \nYou: {game_state['user_score']} \nBot: {game_state['bot_score']}\n"

        if game_state["game_over"]:
            response+=self.final_result()

        return response

    def final_result(self):
        if game_state["user_score"]>game_state["bot_score"]:
            return "Game Over. You won the game"
        elif game_state["bot_score"]>game_state["user_score"]:
            return "Game Over. Bot Won the game"
        else:
            return "Game Drawn"
               
def main():
    agent=RefereeAgent()
    print(agent.explain_rules())
    while not game_state["game_over"]:
        user_input=input("You: ")
        response=agent.respond(user_input)
        print("Bot:",response)

if __name__=="__main__":
    main()
