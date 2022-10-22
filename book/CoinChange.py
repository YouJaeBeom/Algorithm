def coinchange(coin):
    coin_500=0
    coin_100=0
    coin_50=0
    coin_10=0
    coin_1=0
    while(coin>=1):
        if(coin>=500):
            coin_500=coin_500+1
            coin=coin-500
        elif (500> coin >= 100):
            coin_100 = coin_100 + 1
            coin = coin - 100
        elif (100>coin >= 50):
            coin_50 = coin_50 + 1
            coin = coin - 50
        elif (50>coin >= 10):
            coin_10 = coin_10 + 1
            coin = coin - 10
        elif (10>coin >= 1):
            coin_1 = coin_1 + 1
            coin = coin - 1

    return coin_500,coin_100,coin_50,coin_10,coin_1

coin=int(input("거스름돈 액수:"))
coin_500,coin_100,coin_50,coin_10,coin_1=coinchange(coin)
print("coin_500 :",coin_500)
print("coin_100 :",coin_100)
print("coin_50 :",coin_50)
print("coin_10 :",coin_10)
print("coin_1 :",coin_1)
