# Day 3 Exercise
name1 = input("What is your full name? ").lower()
name2 = input("What is his/her full name? ").lower()
combined = name1 + name2
T_count = combined.count("t")
R_count = combined.count("r")
U_count = combined.count("u")
E_count = combined.count("e")
true = T_count + R_count + U_count + E_count
L_count = combined.count("l")
O_count = combined.count("o")
V_count = combined.count("v")
E2_count = combined.count("e")
love = L_count + O_count + V_count + E2_count
Love_Score = int(str(true) + str(love))
print(f"\nT occurs {T_count} times\nR occurs {R_count} times\nU occurs {U_count} times\nE occurs {E_count} times\nSubtotal:{true}")
print(f"\nL occurs {L_count} times\nO occurs {O_count} times\nV occurs {V_count} times\nE occurs {E2_count} times\nSubtotal:{love}")
print(f"Your Love Score is {Love_Score}")
if Love_Score > 10 or Love_Score < 90:
    print(f"Your score is {Love_Score}. You go like coke and mentos!")
elif 40 <= Love_Score <= 50:
    print(f"Your score is {Love_Score}. You are alright together.")
else:
    print(f"Your score is {Love_Score}.")