from string import punctuation
import regex


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.origins = None
        self.gender = None
        self.diagnose = None
        self.reason = ""
        self._stage = 0

    def __repr__(self):
        return self.name

    def _dir(self):
        return [attr for attr in dir(self) if '_' not in attr]
    
    def _unknowns(self):
        all_attrs = self._dir()
        unknowns = []
        for attr in all_attrs:
            if getattr(self, attr) == None:
                unknowns.append(attr)
        return unknowns




def get_input(message='', allow_empty=False, empty_request='Please enter a non-empty sequence.'):
    """Returns an input from user stripped from space characters
        :param message: (str) Message to ask for an input from user
        :param allow_empty: (bool) Flag to allow or not empty inputs (enter key pressed)
        :param empty_requests: (str) Message to append when asking for a non-empty input

        :returns: (str) user input
    """

    in_str = input(f'{message}\n> ').strip()
    if not allow_empty:
        while len(in_str) == 0:
            in_str = input(f'{message} {empty_request}\n> ').strip()
    
    if in_str == 'q':
        flag = False
    else:
        flag = True
    return flag, in_str

def format_(s, attr):
    str_with_info = s.replace('{}', attr)
    return str_with_info


def parse_reason(s):
    pairs = [
        ("I have", "you have"),
        ("I've", "you have"),
        ("I am", "you are"),
        ("I'm", "you are"),
    ]

    for s_orig, s_end in pairs:
        s = s.replace(s_orig, s_end)
    
    return s.lower()


def parse_condition(s):
    kws = ['feel', 'feeling ', 'am', "'m", "'ve", 'been', 'very', 'extremely', 'super', 'doing']

    for punct in punctuation:
        if punct != "'" and punct in s:
            s = s.replace(punct, ' ')
    
    words = s.split()

    # print(words)

    if len(words) == 1:
        return words[0]
    
    last_idx = -1
    last_kw = ""
    for kw in kws:
        
        if "'" in kw:
            for w in words:
                if kw in w:
                    kw = w
                    

        if kw in words and words.index(kw) > last_idx:
            last_kw = kw
            last_idx = words.index(kw)

    return words[last_idx + 1]



if __name__=="__main__":
    print(0)