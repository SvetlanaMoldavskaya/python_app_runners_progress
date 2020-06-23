# 6. An athlete goes running every day. On the first day his result was a km. Every day they were increasing their result by 10 %. Define the day (nutural number), n which the overall result makes up no less than b km. The program should take in parameters a and b, and output the number of the day.

# The for statement iterates through a collection or iterable object or generator function. The while statement simply loops until a condition is False. ... This gives us a data structure tailor-made for the for statement.

def runner(a, b):
    day = 1
    this_day = a
    print("On day {} you have run {} kilometers.".format(day, this_day))
    while this_day * 1.1 < b:
        day += 1
        this_day = this_day * 1.1
        print("On day {} you have run {} kilometers.".format(day, this_day))
        #  b += 1. Which will reassign b to b+1 . That is not an increment operator, because it does not increment b , it reassigns it.
        # '{} {}'.format('one', 'two')
    else:
        day += 1
        this_day = this_day * 1.1
        # this_day * 10 / 100 OR this_day * 1.1
        print("Congrats! On day {} you have run your max of {} kilometers.".format(
            day, this_day))

runner(1, 20)
