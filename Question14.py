s=int(input())
final_score=0

if s<=100:
    final_score=s+7
    if s%2==0:
        final_score=final_score+1
        if s%10==6:
            final_score=final_score+2
        else:
            final_score=final_score
    elif s%10==6:
        final_score=final_score+2

elif s>100 and s<=1000:
    final_score=s+(s/4)
    if s%2==0:
        final_score=final_score+1
        if s%10==6:
            final_score=final_score+2
        else:
            final_score=final_score

elif s>1000:
    final_score=s+(0.15*s)
    if s%2==0:
        final_score=final_score+1
        if s%10==6:
            final_score=final_score+2
        else:
            final_score=final_score
print(final_score)
