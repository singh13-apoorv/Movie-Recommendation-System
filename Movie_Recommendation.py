import matplotlib.pyplot as plt 
from selenium import webdriver
import time
while True:
    print("*******Recommendation system of movies:*******")
    x=int(input("Menu:\n1.Genre\n2.Actor/Actress\n3.Language\n4.Exit\nChoice:"))
    if x==1:
        gen = input("\nEnter the Genre :")
        driver = webdriver.Chrome()    
        driver.get("https://www.imdb.com/search/title/?genres="+gen+"&groups=top_250&sort=user_rating,desc")
        rating = driver.find_elements_by_tag_name("strong")
        y = []
        rateFinal=[]
        movie=driver.find_elements_by_class_name("lister-item-header")
        tick_label = [i.text for i in movie]
        print("Scrapped Movies-")
        for i in tick_label:
            print(i)
        for i in range(2,len(rating)):
            y.append(rating[i].text)
        y=[float(i) for i in y]
        # print(y)
        x = [i for i in range(1,len(y)+1)]
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ab = [i[0:2] for i in tick_label]
        plt.bar(x, y, tick_label = ab, width = 0.8, color = ['red', 'green']) 
        r = tick_label[y.index(max(y))]
        plt.xlabel(f'Movies \n So, the Recommended movie Acc. to viewers rating is - {r}') 
        plt.ylabel('Ratings')
        plt.title(f'Recommendations of movies according to {gen} ')
        for i in range(0,len(y)):
            ax.annotate(y[i], xy=(x[i], y[i]), xytext=(i+1,max(y)+1.5),arrowprops=dict(facecolor='white', shrink=0))
        plt.show()
    elif x==2:
        act=input("Enter any Actor/Actress:")
        driver=webdriver.Chrome()
        driver.get("https://www.google.com/#q="+act+" movies list imdb")
        driver.maximize_window()
        driver.find_element_by_xpath("//h3[@class='LC20lb DKV0Md']").click()
        rating = driver.find_elements_by_xpath("//div[@class='ipl-rating-star small']")
        y = []
        rateFinal=[]
        movie=driver.find_elements_by_class_name("lister-item-header")
        tick_label = [i.text for i in movie]
        print("Scrapped Movies-")
        for i in tick_label:
            print(i)
        for i in range(0,len(rating)):
            y.append(rating[i].text)
        y=[float(i) for i in y]
        print(y)
        print(len(y))
        x = [i for i in range(1,len(y)+1)]
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ab = [i[0:2] for i in tick_label]
        plt.bar(x, y, tick_label = ab, width = 0.8, color = ['red', 'green']) 
        r = tick_label[y.index(max(y))]
        plt.xlabel(f'Movies \n So, the Recommended movie Acc. to viewers rating is - {r}') 
        plt.ylabel('Ratings')
        plt.title(f'Recommendations of movies according to {act} ')
        for i in range(0,len(y)):
            ax.annotate(y[i], xy=(x[i], y[i]), xytext=(i+1,max(y)+1.5),arrowprops=dict(facecolor='white', shrink=0))
        plt.show()
    elif x==3:
        lan=input("Enter the language::")
        driver=webdriver.Chrome()
        driver.get("https://www.google.com/#q="+"imdb "+lan+" movies 2019")
        driver.maximize_window()
        driver.find_element_by_xpath("//h3[@class='LC20lb DKV0Md']").click()
        rating = driver.find_elements_by_xpath("//div[@class='ipl-rating-star small']")
        y = []
        rateFinal=[]
        movie=driver.find_elements_by_class_name("lister-item-header")
        tick_label = [i.text for i in movie]
        print("Scrapped Movies-")
        for i in tick_label:
            print(i)
        for i in range(0,len(rating)):
            y.append(rating[i].text)
        y=[float(i) for i in y]
        print(y)
        print(len(y))
        if(len(y)<len(tick_label)):
            for i in range(0,len(tick_label)-len(y)):
                y.append(8)
        x = [i for i in range(1,len(y)+1)]
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ab = [i[0:2] for i in tick_label]
        plt.bar(x, y, tick_label = ab, width = 0.8, color = ['red', 'green']) 
        r = tick_label[y.index(max(y))]
        plt.xlabel(f'Movies \n So, the Recommended movie Acc. to viewers rating is - {r}') 
        plt.ylabel('Ratings')
        plt.title(f'Recommendations of movies according to {lan} ')
        for i in range(0,len(y)):
            ax.annotate(y[i], xy=(x[i], y[i]), xytext=(i+1,max(y)+1.5),arrowprops=dict(facecolor='white', shrink=0))
        plt.show()
    else:
        exit()
        