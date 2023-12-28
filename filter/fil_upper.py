def str(a):
    if 'A'<=a<='Z':
        return True
    else:
        return False
out=filter(str,'aBc@1567DEfgh')
print(list(out))