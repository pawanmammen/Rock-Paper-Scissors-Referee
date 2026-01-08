AI Game Referee Chatbot – Rock–Paper–Scissors–Plus

Overview
This project implements a stateful conversational chatbot that acts as a referee for a modified Rock–Paper–Scissors game (Rock–Paper–Scissors–Plus). The chatbot enforces game rules, tracks state across turns, and communicates outcomes in natural language.

The design follows Google ADK (Agent Development Kit) principles, separating the system into:
- Agent (decision-making and response generation)
- Tools (deterministic game logic)
- State (persistent memory)


Game Rules
- Best of 3 rounds
- Valid moves:
  - rock
  - paper
  - scissors
  - bomb (can be used once per player)
- Bomb beats all other moves
- Bomb vs bomb results in a draw
- Invalid input wastes the round
- Game ends automatically after 3 rounds


Architecture

State Model
The game state is stored outside the agent and persists across turns.

Tracked fields:
- round
- user_score
- bot_score
- user_bomb
- bot_bomb
- game_over


Tools (Deterministic Logic)
The following functions act as explicit tools:
- validate_move: validates user input and bomb usage
- resolve_round: determines the round winner
- update_state: updates scores, rounds, and termination
- bot_choose_move: selects a valid bot move


Agent
RefereeAgent represents the LLM-style conversational agent.

Responsibilities:
- Interpret user input (including simple natural language like “I choose paper”)
- Invoke tools to validate and resolve moves
- Generate human-readable responses
- Announce the final game result

The agent does not directly modify state; all state changes occur through tools.


Conversational Loop
The chatbot runs in a CLI-based conversational loop:
- User inputs a move
- Agent responds with round outcome
- Loop continues until the game ends


Running the Project

Requirements
- Python 3.8 or higher

Steps
1. Place the code in a file (e.g. chatbot_adk.py)
2. Run: python chatbot_adk.py
3. Enter moves such as:
   rock
   paper
   scissors
   bomb
   I choose paper


Tradeoffs
- Bot move selection is random
- Intent parsing is keyword-based
- CLI interface is used instead of a graphical UI


Possible Improvements
- More robust natural language understanding
- Smarter bot strategy
- Multi-agent separation
- Integration with a real LLM backend


Summary
This project demonstrates:
- Stateful conversational agent design
- Clear separation of agent, tools, and state
- Deterministic rule enforcement
- ADK-style architecture suitable for production AI systems
