import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token =  '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' 

    def getUser(self, username):
        response = requests.get(self.api_url +'/users/'+ username)
        return response.json()

    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()

    def createRepository(self, name):
        response = requests.post(self.api_url+'/user/repos?access_token='+self.token, json={
            "name": name,
            "description": "This is my first repository",
            "hompage": "https://github.com",
            "privaate": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()


github = Github()


while True:
    secim = input('1- Find User\n2- Get Reposistories\n3- Create Repository\n4- Exit \nSeçim: ')
    if secim == '4':
        break
    else:
        if secim == '1':
            username = input('username: ')
            result = github.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} followeer: {result['followers']}")

        elif secim == '2':
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif secim == '3':
            name = input('Repository name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print('Yanlış Secim')







