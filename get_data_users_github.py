import requests
from urllib.request import urlopen
from PIL import Image

'''Some app that get requests from api.github.com/users'''

def get_usuario(username):
    return requests.get(f'https://api.github.com/users/{username}').json()

def subs(username):
    return requests.get(get_usuario(username)['subscriptions_url']).json()


if __name__ == '__main__':
    usuario = input('nome de usuario do github: ')
    geral = get_usuario(usuario)
    info = subs(usuario)
    sz_info_subs = list(range(len(info)))

    #Screen some main datas from users, setted to pt-BR idiom
    print('Nome: {}\nLinkedin: {}\nLocalização: {}\nTwitter: https://twitter.com/{}'.format(geral['name'],geral['blog'], geral['location'], geral['twitter_username']))

    for n in sz_info_subs:
        tabela = {'Subs':[info[n]['language'], info[n]['name']]}
        print(tabela)
    
    #Show user avatar
    Image.open(urlopen(get_usuario(usuario)['avatar_url'])).show()




