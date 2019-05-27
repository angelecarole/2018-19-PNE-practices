class Seq():
    def __init__ (self, strbase):
        self.strbase = strbase

    def len(self):
        length = len(self.strbase)
        return length

    def complement(self):
        comp = ''
        for i in self.strbase:
            if i == 'A':
                comp += 'T'
            elif i == 'T':
                comp += 'A'
            elif i == 'C':
                comp += 'G'
            elif i == 'G':
                comp += 'C'
        comp_seq = Seq(comp)
        return comp_seq

    def reverse(self):
        reverse1 = self.strbase[::-1]
        reverse = Seq(reverse1)
        return reverse

    def count(self, base):
        return(self.strbase.count(base))


    def perc(self, base):
        total_len = len(self.strbase)
        count = self.strbase.count(base)
        perc = round(100.0*(count/total_len),1)
        return perc