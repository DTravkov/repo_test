movies = [

{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam", #My favourite :)
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]



def is_highrated(name:str):
    for movie in movies:
        if movie["name"] == name:
            return movie['imdb'] > 5.5

print(is_highrated("We Two"))

def get_highrated_list():
    lst = []
    for movie in movies:
        if movie['imdb'] > 5.5:
            lst.append(movie['name'])
    return lst

print(get_highrated_list())


def get_category_list(category:str):
    lst = []
    for movie in movies:
        if movie['category'] == category:
            lst.append(movie['name'])
    if len(lst) == 0:
        return f"We can't find any info on {category}"
    else:
        return lst

print(get_category_list('Suspense'))

def get_average_imdb():
    imbd_overall = 0
    for movie in movies:
        imbd_overall += movie['imdb']
            
    return imbd_overall / len(movies)

print(get_average_imdb())

def get_average_imdb_category(category:str):
    lst = []
    category_imbd_score = 0
    for movie in movies:
        if movie['category'] == category:
            lst.append(movie['name'])
            category_imbd_score += movie['imdb']
    if len(lst) == 0:
        return f"We can't find any info on {category}"
    else:
        return category_imbd_score / len(lst)

print(get_average_imdb_category("Suspense"))