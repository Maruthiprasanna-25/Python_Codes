# **SUB STRING**

def sub_string_count(string,sub_string):
    count=0
    end=len(sub_string)
    start=0
    while end<=len(string):
        if sub_string==string[start:end]:
            count+=1
        start+=1
        end+=1
    return count
string=input().strip()
sub_string=input().strip()
res=sub_string_count(string,sub_string)
print(res)
