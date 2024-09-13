def soma(*nums):
    total = 0
    
    for n in nums:
        total += n
    return total

def pessoa(**kwargs):
    print(f"Nome:{kwargs["nome"]}")
    print(f"Idade: {kwargs["idade"]}")