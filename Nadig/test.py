from os import listdir

fs = [f for f in listdir('.') if f[-4:]=='.cha']
print()
for f in fs:
    ls = [l for l in open(f) if l[:1]not in'%@']
    print(ls)
    break

grep "xxx" * | cut -c3 - | sort | uniq -c
grep "\&\w*" * | grep -v "%mor"

# then exclude &=laughs &c. ig
