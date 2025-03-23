# Slotmachine-Game

This is a simple text-based slot machine game built using Python. The game allows players to place bets, spin the slot machine, and win payouts based on matching symbols.

# Features

-Uses emoji symbols (🍒, 🍉, 🍋, 🔔, ⭐)
-Allows players to place bets
-Randomized spins using Python's random module
-Calculates payouts based on matching symbols
-Tracks player balance throughout the game

# How to Play

-Start with a balance of 100.
-Place a bet amount (must be within available balance).
-The slot machine spins and displays three symbols.
-If all three symbols match, you win a payout based on the symbol type.
-If no match occurs, you lose your bet.
-The game continues until you run out of balance.

# Payout Structure

🍒 → Bet x3

🍉 → Bet x4

🍋 → Bet x5

🔔 → Bet x6

⭐ → Bet x7



Example Game Play

*******************************
Symbols: |🍒|🍉|🍋|🔔|⭐
*******************************
Current Balance: R100
Place your bet amount: R10
Spinning.....
🍋 | 🍋 | 🍋
You won! R50
