    
import datetime

class Soluton:
    def threeSumClosest1(self, num_ori, target):
        num = sorted(num_ori)
        # result = 0
        if len(num) < 3:
            return
        else:
            result = (num[0] + num[1] + num[2])
            min_num = abs(target - (num[0] + num[1] + num[2]))
            l1 = min_num
            l2 = min_num
        for i in range(0,len(num)-2):
            if min_num == 0:
                break
            for j in range(i+1,len(num)-1):
                if min_num == 0:
                    break;
                for k in range(j+1,len(num)):
                    l1 = l2
                    l2 = abs(target - (num[i] + num[j] + num[k]))
                    if l2 > l1:
                        break;
                    if abs(target - (num[i] + num[j] + num[k])) < min_num:
                        min_num = abs(target - (num[i]+num[j]+num[k]))
                        result = num[i] + num[j] + num[k]
                        # print "Using Method 1: num[%d]=%d num[%d]=%d num[%d]=%d min_num =%d" %(i, num[i], j,num[j],k,num[k],min_num)
                        if min_num == 0:
                            break;
                    
        return result


    def threeSumClosest(self, num_ori, target):
        num = sorted(num_ori)
        # print num
        min_num = 0
        if len(num) < 3:
            return
        else:
            min_num = abs(target - (num[0] + num[1] + num[2]))
            result = num[0] + num[1] + num[2]
        min_temp = min_num
        for i in range(0,len(num)-2):
            # print "i = %d begin" %(i)
            if min_num == 0:
                break
            start_i = i+1
            end_i = len(num)-1
            j = (start_i + end_i)/2
            while start_i < end_i:
            # for j in range(i+1, len(num)-1):
                # print "i = %d j = %d"%(i,j)
                # l1 = l2
                # l2 = min_temp
                # if l2 > l1:
                #     break;
                if min_num == 0:
                    break
                k = self.find_third(num,i,j,target)
                
                min_temp = abs(target - num[i] - num[j] - num[k])
                if min_num > min_temp:
                    min_num = min_temp
                    result = num[i] + num[j] + num[k]
                if min_temp < 0:
                    start_i = j + 1
                else:
                    end_i = j - 1
                # print "min_temp=%d target: %d num[%d]=%d num[%d]=%d num[%d]=%d min_num =%d" %(min_temp, target,i, num[i], j,num[j],k,num[k],min_num)
                j = (start_i + end_i)/2

                    # print abs(target - (num[i] + num[j] + num[k])),
                    # print '%d %d %d' %(num[i], num[j], num[k])
                # temp = target - num[i] - num[j]
                # print "temp=%d target: %d num[%d]=%d num[%d]=%d " %(temp, target,i, num[i], j,num[j]),
                # start = j + 1
                # end = len(num)-1
                # k = (start + end)/2
                # temp_k = num[k]
                # temp_r = abs(temp_k - temp)
                # while start < end:
                #     # if temp_r < abs(num[k] - temp):
                #     #     temp_r = abs(num[k] - temp)
                #     #     temp_k = num[k]
                #     if temp_r == 0:
                #         break
                #     if num[k] < temp:
                #         start = k + 1
                #     else:
                #         end = k - 1
                #     k = (start + end)/2
                # min_temp = abs(target - (num[i] + num[j] + temp_k))
                # print "num[k]=%d, min_temp=%d, min_num=%d"%(num[k], min_temp, min_num)

                # if min_num > min_temp:
                #     # print 'find min'
                #     min_num = min_temp  
                #     result = num[i] + num[j] + temp_k
                # if min_temp < 

        return result

    def find_third(self, num, i, j, target):
        temp  = target - num[i] - num[j]
        # print "findingK_temp=%d, i=%d,j=%d"%(temp,i,j),
        start = j+1
        end = len(num)-1
        k = (start + end)/2
        temp_r = abs(temp - num[k])
        temp_index = k
        while start < end:
            if abs(temp - num[k]) < temp_r:
                temp_r = abs(temp - num[k])
                temp_index = k
            if num[k] < temp:
                start = k + 1
            else:
                end = k - 1
            k = (start + end)/2
        if  temp_index >= len(num):
            temp_index = len(num) - 1
        if temp_index <= j+1:
            temp_index = j+1
        # print 'returned K = ' + str(k) + 'len(num) = ' + str(len(num))
        return temp_index



def main():
    # num = [1,1,-1,-1,3]
    # num = [-1,0,1,2,-1,-4]
    num = [1,2,4,8,16,32,64,128]
    # num = [43,75,-90,47,-49,72,17,-31,-68,-22,-21,-30,65,88,-75,23,97,-61,53,87,-3,33,20,51,-79,43,80,-9,34,-89,-7,93,43,55,-94,29,-32,-49,25,72,-6,35,53,63,6,-62,-96,-83,-73,66,-11,96,-90,-27,78,-51,79,35,-63,85,-82,-15,100,-82,1,-4,-41,-21,11,12,12,72,-82,-22,37,47,-18,61,60,55,22,-6,26,-60,-42,-92,68,45,-1,-26,5,-56,-1,73,92,-55,-20,-43,-56,-15,7,52,35,-90,63,41,-55,-58,46,-84,-92,17,-66,-23,96,-19,-44,77,67,-47,-48,99,51,-25,19,0,-13,-88,-10,-67,14,7,89,-69,-83,86,-70,-66,-38,-50,66,0,-67,-91,-65,83,42,70,-6,52,-21,-86,-87,-44,8,49,-76,86,-3,87,-32,81,-58,37,-55,19,-26,66,-89,-70,-69,37,0,19,-65,38,7,3,1,-96,96,-65,-52,66,5,-3,-87,-16,-96,57,-74,91,46,-79,0,-69,55,49,-96,80,83,73,56,22,58,-44,-40,-45,95,99,-97,-22,-33,-92,-51,62,20,70,90]
    # num = [6,-34,70,-43,1,-74,56,-18,-47,44,43,-96,-81,-65,68,60,-9,59,-52,32,61,41,31,56,94,-53,-94,-35,38,55,20,-12,40,-41,-38,-10,10,16,-42,85,-38,4,-18,72,-39,95,-73,-55,-43,-70,0,46,97,-84,-67,-5,-37,68,15,-78,31,-80,-44,-48,-28,-100,-97,-4,6,-29,-21,-76,10,46,-49,80,27,-16,92,-90,-82,-13,-67,70,37,79,34,-48,-65,70,-15,60,6,45,41,16,56,67,-79,28,2,39,28,-80,-13,-72,-97,-37,-8,-100,-83,-37,-77,26,74,-36,-28,-78,-95,-81,39,-1,-50,4,87,-39,-52,6,-13,-16,-53,-95,94,2,-61,61,-1,-68,-33,-76,-41,54,57,-54,-24,-55,88,-58,53,0,76,-46,56,-95,17,-74,50,84,-19,-9,39,20,46,40,38,-46,-68,57,38,-44,-53,80]
    # num = [-12,-44,-67,-65,17,17,-80,73,51,46,-48,-43,-31,17,68,25,79,65,-41,18,-68,-7,29,-19,-48,3,-67,73,-57,-90,12,37,-16,-1,-65,47,53,-79,0,-62,-96,-10,-79,-25,38,93,28,6,99,68,-25,-27,-1,-61,70,-50,-54,-93,43,-34,31,98,-56,-70,44,49,-52,13,15,55,63,16,-30,-15,-25,87,75,81,19,17,88,-99,9,-92,-52,75,-16,97,-99,-86,60,-45,-88,99,75,36,-82,-67,-12,-47,37,-44,-45,67,85,-32,57,-11,-35,-51,-25,-38,54,-30,96,-62,-31,53,-79,-19,37,-73,95,-38,-60,72,-8,-24,-46,-61,63,-41,95,37,-79,-1,74,-9,92,97,-34,-69,-43,38,79,64,21,68,64]
    # num = [96,-52,73,25,-95,-5,74,-72,-81,77,-68,-14,12,-35,75,23,-98,41,-56,1,-69,77,86,63,-78,2,65,-67,46,-23,32,90,-19,32,-63,92,-73,7,-82,-57,41,3,-74,14,-3,73,-16,98,59,-77,61,86,-1,-25,-95,-75,74,-39,81,-100,57,86,0,-40,44,-13,-16,-72,24,-100,10,53,-85,-64,11,50,1,39,51,-60,-95,32,-4,-27,32,-79,66,93,56,16,52,-67,67,-54,83,79,53,-54,-81,-51,73,-21,94,-89,2,-82,-2,-74,-52,-53,7,11,-75,-84,78,-100,-31,89,1,-40,-14,24,69,18,-57,21,35,-92,-30,63,76,-24,84,64,-22,-20,57,85,40,-79,-7,95,99,-85,-93,3,76,-41,-73,76]
    s = Soluton()
    print abs(-2)
    print range(0,len(num))
    starttime = datetime.datetime.now()
    print s.threeSumClosest1(num,82)
    end1time = datetime.datetime.now()
    print s.threeSumClosest(num,82)
    endtime = datetime.datetime.now()
    print str((end1time - starttime).microseconds) + ' ' + str((endtime - end1time).microseconds)


if __name__=='__main__':
    main()