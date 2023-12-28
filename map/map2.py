def view(a):
        if type (a) in [list,tuple,set,dict]:
            return len(a)
        else:
            return a
a=map(view,[1,(4,5),[7,9],{1:2}])
print(list(a))