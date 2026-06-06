def store_score(score):
    with open("score_vault.txt", "w") as f:
           score =str(score)
           f.write(score)

def get_high_score():
    try:
      with open("score_vault.txt", "r") as file:
          score=file.read()
          return score
    except FileNotFoundError:
          return 0


