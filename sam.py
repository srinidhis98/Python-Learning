# print('Welcome to Tic Tac Toe!')
# while True:
#     board = [' ']* 10
#     p1_marker, p2_marker = player_input()
#     turn = choose_first()
#     print(f'{turn} will start')
#     play_round = input("Start the Game YES or NO")
#     if play_round[0].lower() == 'y':
#         game_on = True
#     else:
#         game_on = False

#     while game_on:
#         if(turn == 'Player1'):
#             display_board(board)
#             pos = player_choice(board)
#             place_marker(board, p1_marker, pos)
#             if(win_check(board, p1_marker)):
#                 display_board(board)
#                 print("Congratulations You won")
#                 game_on = False

#             else:
#                 if(full_board_check(board)):
#                     print("The Game is draw")
#                     display_board(board)
#                     break
#                 else:
#                     turn = 'Player2'


#         else:
#             display_board(board)
#             pos = player_choice(board)
#             place_marker(board, p2_marker, pos)
#             if(win_check(board, p2_marker)):
#                 display_board(board)
#                 print("Player 2 won")
#                 game_on = False

#             else:
#                 if(full_board_check(board)):
#                     print("The Game is draw")
#                     display_board(board)
#                     break
#                 else:
#                     turn = 'Player1'


#     if not replay():
#         break