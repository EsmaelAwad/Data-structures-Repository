def anagram(s1,s2):
    
    score = 0
    
    for c in s1:
        
        if c in s2:
            score += 1
    if score == len(s2):
        return f"Match pct% : {(score/len(s2))*100}%","The two strings are anagrams"
    else:
        return f"Match pct% : {(score/len(s2))*100}%","The two strings are not anagrams"

print(anagram("ahmed gamal","gamal ahmed"))            