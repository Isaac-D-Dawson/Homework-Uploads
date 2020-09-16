class Friend:
    def __init__(self, name):
        self.name = name
        self.invite = "No party..."
    
    def show_invite(self):
        return(self.invite)

class Party:
    def __init__(self, name):
        self.name = name
        self.observers = []
    
    def add_friend(self, friend):
        self.observers.append(friend)
    def del_friend(self, friend):
        self.observers.pop(self.observers.index(friend))
    
    def send_invites(self, time):
        for i in self.observers:
            i.invite = f"{self.name}: {time}"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."
    print("Coding complete? Let's try tests!")
