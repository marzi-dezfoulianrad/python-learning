def main (hashtags):
    for index in range(len(hashtags)):

        if index == len(hashtags) - 1:
            print(f'{hashtags[index]}', end ='')

        elif index == len(hashtags) - 2:
            print(f'{hashtags[index]} ,and ', end= ' ')

        else:
            print(f'{hashtags[index]}, ', end= '')
        
    print()

hashtags = input("What is in you mind? (split with a ,) ").split(',')

main(hashtags)
