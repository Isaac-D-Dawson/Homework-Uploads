class Text:
    def __init__(self):
        self.text = ""
        self.font = ""

    def write(self, text):
        self.text = f"{self.text}{text}"
        #print(f"Text set as = {self.text}")
    def set_font(self, font):
        self.font = f"[{font}]"
        #print(f"Font set as = [{font}]")
    
    def show(self):
        return(f"{self.font}{self.text}{self.font}")
    
    def restore(self, targ):
        self.text = targ[0]
        self.font = targ[1]

class SavedText:
    def __init__(self):
        self.archive = []
        #self.limit = 10
    
    def save_text(self, targ):
        self.archive.append([targ.text, targ.font])
    
    def get_version(self, ver):
        return(self.archive[ver])
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()
    
    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
    
    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")
