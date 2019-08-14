class Key(int):
    '''musical key represented by number
    A0 to 1, C4 to 40, A4 to 49
    A♯0, Ash0, Ais0 to 2; B♭0, Bfl0, Bes0 to 2'''
    @staticmethod
    def nti(s):
        '''notation to integer
        A0 to 1, C4 to 40, A4 to 49
        Ash0, Ais0 to 2; Bfl0, Bes0 to 2
        '''
        s = s.lower()
        match = dict(c=0, d=2, e=4, f=5, g=7, a=9, b=11)
        key = s[:-1]
        octave = int(s[-1])
        accidental = key[1:]
        i = octave*12 + match[key[0]] - 8
        if not accidental:
            return i
        if accidental in ('♯', '#', 'sh', 'is'):
            return i+1
        if accidental in ('♭', 'b', 'fl', 'es', 's'):
            return i-1
        return i

    def __new__(cls, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], str):
            return super().__new__(cls, cls.nti(args[0]))
        return super().__new__(cls, *args, **kwargs)

    def __repr__(self):
        lst = ['G♯', 'A', 'A♯', 'B', 'C', 'C♯', 'D', 'D♯', 'E', 'F', 'F♯', 'G']
        return lst[self%12]+str((self+8)//12)+(
            f'; {str(self)}(A0); {str(self-40)}(C4)')
