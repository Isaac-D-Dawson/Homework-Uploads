class VoiceCommand:
    def __init__(self, channel_list):
        self.channel_list   = channel_list
        self.curr_chan      = 0
        self.chan_range     = len(channel_list)-1
    
    def first_channel(self):
        self.curr_chan = 0
        return(self.channel_list[0])
    def last_channel(self):
        self.curr_chan = self.chan_range
        return(self.channel_list[-1])
    
    def turn_channel(self, n):
        self.curr_chan = n-1
        return(self.channel_list[self.curr_chan])
    
    def next_channel(self):
        self.curr_chan += 1
        if self.curr_chan > self.chan_range:
            self.curr_chan = 0
        return(self.channel_list[self.curr_chan])
    def previous_channel(self):
        self.curr_chan -= 1
        if self.curr_chan < 0:
            self.curr_chan = self.chan_range
        return(self.channel_list[self.curr_chan])
    def current_channel(self):
        return(self.channel_list[self.curr_chan])
    
    def is_exist(self, targ):
        if isinstance(targ, int) == True:
            if int(targ) in range(0, self.chan_range):
                return("Yes")
            else:
                return("No")
        elif isinstance(targ, str) == True:
            if str(targ) in self.channel_list:
                return("Yes")
            else:
                return("No")
        else:
            return("No")
        


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)
    
    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"
    print("Coding complete? Let's try tests!")
