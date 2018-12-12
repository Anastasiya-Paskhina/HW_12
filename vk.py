import requests


class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return 'https://vk.com/id' + self.user_id

    def my_friends(self):
        params = {
            'user_id': self.user_id,
            'access_token': '643664a007e9e890893d3fb5c109d24a0b6ad0ff9c17d9daf529b278f0a8d213d8a7462b75c20a1cdebb0',
            'v': '5.92',
            'fields': 'domain'
        }
        response = requests.get('https://api.vk.com/method/friends.get', params)
        two_friends_data = response.json()
        two_friends_set = set()
        for friend in two_friends_data['response']['items']:
            two_friends_set.add(friend['id'])
        return two_friends_set

    def __and__(self, other):
        general_friends = list(self.my_friends() & other.my_friends())
        friends_list = [User(i) for i in general_friends]
        print(friends_list)


if __name__ == "__main__":
    user1 = User('1461201')
    user2 = User('18132541')
    user1 & user2
    print(user1)
    print(user2)