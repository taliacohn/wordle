class ReadFile:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path) as f:
                line = f.readline()
                fields = []
                while line:
                    fields += line.split()
                    line = f.readline()
            return fields
        except FileExistsError:
            print('file not found')

        return fields
        
    # for line in f: #process words separately - split line into words
    #         next clean for punctuation before split - after you split, need to call for each word separately 
    #         clean_line = ''.join([ch for ch in line if ch not in string.punctuation])
    #         clean_line = ''.join([ch for ch in line if ch.alpha and ch.space])
    #         now call split to get all the words
    #         words = clean_line.lower().split() #better to call lower before split, otherwise you need to call lower for each word
            
    
     # def choose_word(self):
    #     try:
    #         with open(self.file_path) as f:
    #             line = f.readline()
    #             while line:
    #                 fields = line.split()
    #                 choice = random.choice(fields)
    #                 line = f.readline()
    #         return choice
    #     except FileNotFoundError:
    #         print('file not found')

    

