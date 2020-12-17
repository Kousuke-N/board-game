import random
cards = [
  3, 3, 3, 3, 3,3,
  5, 5, 5, 5,5,5,5,5,
  8, 8, 8,8,8,8,
  10, 10, 10, 10, 10,10, 10, 10, 10, 10,
  15, 15,15, 15,
  20,20
]
player = [[], [], [], [], []]
player_name = ['根津', '江森', '小池', '津田', '山崎']
cnt = 0

while (True):
  print(f'{player_name[cnt%len(player)]}は引く？：')
  text = input()
  if text == 'y':
    i = random.randint(0, len(cards)-1)
    card = cards.pop(i)
    player[cnt % len(player)].append(card)
    print(f"player card{cnt % len(player)}:{card}")
  if text == 'q':
    break
  for i in range(len(player)):
    print(f"{player_name[i]}:{player[i]}")
  cnt += 1
  print()
