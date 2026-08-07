def movie_review_call():
    def movie_rating(name,collection,mus_bgm,cine_story,acting):
        rating=collect(collection)*0.000000000000000000001+mus_bgm*0.10009999900+cine_story*0.500+acting*0.40089999
        return rating
    def collect(collection):
        num=0.0
        if collection>=1000000000:
            
            num=4.0
        elif collection<1000000000 and collection>1000000:
            num=3.0
        elif collection<1000000 :
            num=2.0
        else:
            pass
        return num
    name=input("Enter the movie name\n")
    collection=float(input("Enter the WORLD-WIDE COLLECTION of the movie\n"))
    while collection<=1000.0:
        collection=float(input(" Give the CORRECT Input\n"))
    mus_bgm=float(input("Rate movie MUSIC AND BACKGROUND MUSIC between 1 to 5 \n"))
    while mus_bgm>5.0 or mus_bgm< 1.0:
        mus_bgm=float(input(" Bro! for real!! \nRate between 1 to 5\n"))
    cine_story=float(input("Rate the movie CINEMATOGRAPHY AND STORY between 1 to 5\n"))
    while cine_story>5.0 or cine_story<1.0:
        cine_story=float(input("ladleeeeeee!! \nragebait mat kar\n asla hum bji rakh te ha\nRate between 1 to 5\n"))
    acting=float(input("Rate the actors OVERALL ACTING PERFORMANCES between 1 to 5\n"))
    while acting>5.0 or acting<1.0:
        acting=float(input("In ki amma behen pe aajaunga inki!!!!\nRate between 1 to 5\n"))
    rating=movie_rating(name,collection,mus_bgm,cine_story,acting)
    rating=round(rating,1)
    rating_percent=(rating/5.0)*100
    rating_percent=round(rating_percent)
    overall_rating=f"The OVERALL RATING of the  movie {name} is {rating}/5  \n in percentage {rating_percent}% "
    print(overall_rating)
    viewers_opinion=''
    if rating_percent>=90.0:
        viewers_opinion=f" Must Watch Movie \n Absolute Cinema!! \n Sureal Experience \n Work of art \n Go and watch '{name}' in Movie Theatres "
        print(viewers_opinion)
    elif rating_percent<90.0 and rating_percent>=80.0:
        viewers_opinion=" Worth the Wait \n Absolutely Justifies the hype \n Worth the expense to watch in Cinemas \n Just go for it"
        print(viewers_opinion)
    elif rating_percent<80.0 and rating_percent>=70.0:
        viewers_opinion=" Ain't that bad \n May attract a Particular group \n worth on Online streaming services"
        print(viewers_opinion)
    elif rating_percent<70.0 and rating_percent>=55.0:
        viewers_opinion=" Watch if you have absolutly nothing to do \n Watch and Just forget \n Expect nothing for it"
        print(viewers_opinion)
    else:
        viewers_opinion=" Ye  Sab Kya Dekhna Padhraha hai  \n VRO, padhai likhai karo IAS  'Y'AS bano aur desh ko samalho \n movie dekh ke akhoon se khoon nikle ga"
        print(viewers_opinion)
    returning_list=[name,collection,rating,rating_percent,overall_rating,viewers_opinion]
    return returning_list
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import mysql.connector as c
con=c.MySQLConnection(user='root',host="localhost",password="Admin@24",autocommit=True)
db_cursor=con.cursor()
st1="CREATE DATABASE IF NOT EXISTS reviews;"
db_cursor.execute(st1)
st="USE reviews;"
db_cursor.execute(st)
db_cursor.execute("DROP TABLE IF EXISTS movie_reviews;")
st2="CREATE TABLE  IF NOT EXISTS movie_reviews (Movie_Name VARCHAR(25) NOT NULL,World_Wide_Collection INT,Rating FLOAT,Rating_Percent int,Overall_Review TEXT,Viewers_opinion TEXT);"
db_cursor.execute(st2)
while True:
    print("Enter 1 for Inserting MOVIE REVIEW Data\n")
    print("Enter 2 for Exit")
    c=int(input("Enter your choice\n"))
    if c==1:
        review_list=movie_review_call()
        name=review_list[0]
        collection=review_list[1]
        rating=review_list[2]
        rating_percent=review_list[3]
        overall_rating=review_list[4]
        viewers_opinion=review_list[5]
        '''  st3="INSERT INTO movie_reviews VALUES('{}',{},{},{},'{}','{}');".format(name,collection,rating,rating_percent,overall_rating,viewers_opinion)
        db_cursor.execute(st3)'''
        st3 = "INSERT INTO movie_reviews VALUES(%s, %s, %s, %s, %s, %s)"
        data = (name, collection, rating, rating_percent, overall_rating, viewers_opinion)
        db_cursor.execute(st3, data)
        print("Review successfully added to database!")
    elif c==2:
        break
    else:
        print("Worng Inputs\nWrite the correct choices ")
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
