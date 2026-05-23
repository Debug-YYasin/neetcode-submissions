class Solution:

    def encode(self, strs: List[str]) -> str:

        enc_str = ""
        for s in strs:
            count = 0
            for c in s:
                count +=1
            
            if s == "":
                enc_str += str(0) + "#"
            else:
                enc_str += str(count) + "#" + s

        return enc_str

            


    def decode(self, s: str) -> List[str]:

        strl = []
        cstring = ""
        n = ""
        i = 0

        while i < len(s):

            if s[i] == "#":
                counter = int(n)
                if counter == 0:
                    cstring = ""
                else:
                    cstring += s[(i + 1) : (i + 1 + counter)]
                
                i += counter + 1
                strl.append(cstring)
                n = ""
                cstring = ""
            else:
                n += s[i]
                i += 1

        return strl

                    




