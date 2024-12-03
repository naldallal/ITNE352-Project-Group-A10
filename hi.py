from newsapi import NewsApiClient
import json
name="uuu"
news = NewsApiClient(api_key='d9968ffc1e7f4b02b859492ab750f911')
request = "headline-country-us"
requestList = request.split("-")
if requestList[0] == "headline":
    if requestList[1]=="keyword":
        response = news.get_top_headlines(q=requestList[2])
    elif requestList[1]=="category":
        response = news.get_top_headlines(category=requestList[2])
    elif requestList[1]=="country":
        response = news.get_top_headlines(country=requestList[2])
    elif requestList[1]=="all":
        response = news.get_top_headlines()
elif requestList[0]=="source":
    if requestList[1]=="category":
        response = news.get_sources(category=requestList[2])
    elif requestList[1]=="country":
        response = news.get_sources(country=requestList[2])
    elif requestList[1]=="language":
        response = news.get_sources(language=requestList[2])
    elif requestList[1]=="all":
        response = news.get_sources()
if response: # Extract relevant details and create a list of dictionaries 
    articles = response['articles'] 
    articles = articles[:15]
    fileName = name+'-'+request+'-A10'
    with open(fileName, 'w') as json_file:
        json.dump(articles, json_file, indent=4)
    articles_list = [ 
            { "source_name": article['source']['name'], 
             "author": article['author'], 
             "title": article['title']
            } for article in articles
        ]
    
for i in range(len(articles_list)):
    print(i+1,(articles_list[i]))
# print(articles_list)