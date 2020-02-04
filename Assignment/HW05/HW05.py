class ModelHashMap:
    def __init__(self):
        self._N = 7
        self._table = [ None ] * self._N
    def __setitem__(self, k, v): # if h is a ModelHashMap, called by 'h[k] = v'
        j = hash(k) % self._N
        while self._table[j] != None:
            j = (j+1) % self._N
        self._table[j] = {'key': k, 'value': v}

    def _find_loc(self, k):
        seen =0
        j = hash(k) % self._N
        while self._table[j] == None or self._table[j]['key'] != k:
            seen +=1
            if seen == self._N:
                raise KeyError(f'Could not find key {k} in {type(self).__name__}{self}')
            j = (j+1)%self._N         
        return j
    
    def __getitem__(self, k):  # if h is a ModelHashMap, called by 'h[k]'
        j = self._find_loc(k)         
        return self._table[j]
    
    def __delitem__(self, k):  # if h is a ModelHashMap, called by 'del h[k]'
        j = self._find_loc(k)                           
        self._table[j] = None
        
