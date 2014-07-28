class Solution:
    # @param s, a string
    # @return a string

    # def my_range(self, start, end, direction = True):
    #     if direction:
    #         while start<= end:
    #             yield start
    #             start += 1
    #     else:
    #         while start >= end:
    #             yield start
    #             start += 1

    def reverseWords(self, s):
        result = ''
        flag = True
        s = s.strip()
        new_s = ''
        if s == None:
            return
        else:
            for ac in s:
                if flag:
                    new_s = new_s + ac
                    if ac == ' ':
                        flag = False
                else:
                    if ac !=' ':
                        new_s = new_s + ac
                        flag = True

            words = new_s.split(' ');
            for x in words:
                x = x.strip();
                if x==' ':
                    words.remove(x)
            for x in words:
                print x
            num_of_words = len(words)
            for i in range(0, num_of_words):
                if result == '':
                    result = words[num_of_words-1-i] + result
                else:
                    result = result + ' ' + words[num_of_words - 1- i]
        return result.strip()



def main():
    s = '   a   b '
    cs = Solution();
    s1 = cs.reverseWords(s);
    print s1


if __name__ == '__main__':
    main()