def match(word,pattern,include_chars,exclude_chars) :
    list = []
    if len(word) == len(pattern) :
        for i in range(len(word)) :
            if word[i] != pattern[i] and pattern[i] != "?" :
                return False
            if pattern[i] == "?" :
                list.append(word[i])
                for k in range(len(exclude_chars)) :
                    if word[i] == exclude_chars[k] :
                        return False
        if include_chars != "" :
            for t in include_chars :
                if t in list :
                    list.remove(t)
                else :
                    return False
        return True
    else :
        return False 
exec(input())