import random
import time

def neon_runner():
    # 1. Game Setup
    score = 0
    speed = 1.0  # Seconds between frames
    multiplier = 1.0
    alive = True
    
    # Obstacle types and their dodge commands
    obstacles = {
        "LOW BAR": "jump",
        "HIGH WALL": "slide",
        "SIDE PANEL": "dodge"
    }

    print("--- ⚡ NEON RUNNER ⚡ ---")
    print("Commands: jump, slide, dodge")
    print("The game gets faster every 5 points. Good luck!")
    time.sleep(2)

    # 2. Game Loop
    while alive:
        # Select a random obstacle
        obs_name, correct_cmd = random.choice(list(obstacles.items()))
        
        print(f"\n🚀 SPEED: {multiplier}x | SCORE: {score}")
        print(f"⚠️  APPROACHING: {obs_name}!")
        
        # Start the clock
        start_time = time.time()
        user_input = input("ACTION: ").lower().strip()
        end_time = time.time()
        
        elapsed = end_time - start_time

        # 3. Collision Logic
        if user_input == correct_cmd and elapsed < speed:
            score += 1
            print(f"✅ CLEAN! ({elapsed:.2f}s)")
            
            # 4. Difficulty Scaling
            if score % 5 == 0:
                speed *= 0.8  # Reduce reaction time by 20%
                multiplier += 0.5
                print("🔥 SPEED INCREASED!")
        
        elif elapsed >= speed:
            print(f"\n💥 TOO SLOW! The {obs_name} hit you.")
            alive = False
        else:
            print(f"\n💥 WRONG MOVE! You can't {user_input} a {obs_name}.")
            alive = False

    print(f"\n🏁 GAME OVER | FINAL SCORE: {score}")

# Start the runner
neon_runner()
