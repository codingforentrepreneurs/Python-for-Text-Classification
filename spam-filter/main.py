from preprocessing import make_bag



bow = make_bag("This is awesome")

bow = make_bag("This is bad")

bow = make_bag(["What", "a", "great", "time"])

# bag of words


txt = "This is awesome"

txt2 = "This is bad"

txt3 = "What a great time"

bag_of_words = ["this", "is", "awesome", "bad", 'what', 'a', 'great', 'time']


# this based on positions
txt_bow = [0, 1, 2]

txt2_bow = [0, 1, 3]

txt3_bow = [4, 5, 6, 7]


# one hot array

# txt_oha = [True, True, True, False, False, False, False, False]

# this based on if that position has a value in that string
txt_oha = [1, 1, 1, 0, 0, 0, 0, 0]

tx2_oha = [1, 1, 0, 1, 0, 0, 0, 0]

tx3_oha = [0, 0, 0, 0, 1, 1, 1, 1]



