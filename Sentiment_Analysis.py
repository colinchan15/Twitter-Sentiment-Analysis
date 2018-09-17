##########################
#Colin Chan 
#This program reads prompts a user for two files: one containing the tweets to be analyzed, and another containing keywords + their respective scores
#Then, the program then assigns a dictionary to the keywords with their respective scores
#The program then separates tweets depending on their coordinate locations, and assigns a score to each tweet in that region
#The scores of all tweets in the region are then summed up and printed onto the screen, along with the number of tweets in that region
#NOTE**: region1 = EST, region2 = CST, region3 = MST, region4 = PST

#This section prompts the user for the names of the files containing the keywords + tweets to be analyzed
tweets_file_name = str(input("Please enter the name of the file containing the tweets to be analyzed: "))
keywords_file_name = str(input("Please enter the name of the file containing the keywords: "))
tweets_file = open(tweets_file_name, "r", encoding="utf-8")
keywords_file = open(keywords_file_name, "r", encoding="utf-8")

def main():
    #This section defines dictionary containing keywords + their corresponding scores
    keywords = []
    word_list = []
    number_list = []
    dictionary = {}
    for i in keywords_file.readlines():
        list_split = i.split(",")
        list_stripped = [x.strip() for x in list_split]
        keywords.append(list_stripped)
    file_length = len(keywords)
    for i in range(file_length):
        word = keywords[i][0]
        number = keywords[i][1]
        word_list.append(word)
        number_list.append(number)
    for i in range(file_length):
        dictionary[word_list[i]] = number_list[i]

    #This section reads the tweet file line by line, separating them based on their coordinates
    #depending on their coordinates, each tweet will be added to a list pertaining to the region they are located in (e.g. EST, PST, etc.)
    #the length of each list is also computed
    region1_list = []
    region2_list = []
    region3_list = []
    region4_list = []
    for i in tweets_file.readlines():
        entries = i.split()
        coordinate1 = float(entries[0].strip("[],"))
        coordinate2 = float(entries[1].strip("[],"))
        if coordinate1 <= 49.189787 and coordinate1 >= 24.660845 and coordinate2 <= -67.444574 and coordinate2 >= -87.518395:
            region1_list.append(region_clear(entries))
            region1_length = len(region1_list)
        elif coordinate1 <= 49.189787 and coordinate1 >= 24.660845 and coordinate2 <= -87.518395 and coordinate2 >= -101.998892:
            region2_list.append(region_clear(entries))
            region2_length = len(region2_list)
        elif coordinate1 <= 49.189787 and coordinate1 >= 24.660845 and coordinate2 <= -101.998892 and coordinate2 >= -115.236428:
            region3_list.append(region_clear(entries))
            region3_length = len(region3_list)
        elif coordinate1 <= 49.189787 and coordinate1 >= 24.660845 and coordinate2 <= -115.236428 and coordinate2 >= -125.242264:
            region4_list.append(region_clear(entries))
            region4_length = len(region4_list)

    #each list is then analyzed tweet-by-tweet by the keyword_check function to assign a "happiness score" to each tweet - depending on the words in the tweet
    #these happiness scores are then put into a list, and totalled together
    #finally, all the totalled scores for a particular region are summed and assigned to a "region(n)_score"
    region1_score = region_score(region1_length, region1_list, dictionary)
    region2_score = region_score(region2_length, region2_list, dictionary)
    region3_score = region_score(region3_length, region3_list, dictionary)
    region4_score = region_score(region4_length, region4_list, dictionary)

    #the scores + number of tweets in each region are printed onto the screen
    print("The happiness score and number of tweets in EST, respectively, is: ", region1_score, "and ", region1_length)
    print("The happiness score and number of tweets in CST, respectively, is: ", region2_score, "and ", region2_length)
    print("The happiness score and number of tweets in MST, respectively, is: ", region3_score, "and ", region3_length)
    print("The happiness score and number of tweets in PST, respectively, is: ", region4_score, "and ", region4_length)

def keyword_check(list, dictionary):
    #this function compares the words in each tweet to the dictionary and then assigns a "happiness score" for the tweet
    score_list = []
    total_score = 0
    for i in list:
        if i in dictionary:
            score = dictionary[i]
            score_list.append(score)
    for i in score_list:
        total_score += int(i)
    return(total_score)

def region_score(region_length, region_list, dictionary):
    #this function takes all the "happiness scores" in a particular region and sums them together to produce a final "happiness score" for the region
    region_total = 0
    for i in range(region_length):
        region_total += (keyword_check(region_list[i],dictionary))
    return(region_total)

def region_clear(entries):
    #this function takes a tweet and converts it into lower case letters, and strips them of punctuation using list comprehension
    region_lower = [w.lower() for w in entries[5:]]
    region_stripped = [x.strip("#.!(): ") for x in region_lower]
    return(region_stripped)

main()

tweets_file.close()
keywords_file.close()
