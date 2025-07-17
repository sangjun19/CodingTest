def solution(n, bans):
    def string_to_order(s):
        order = 0
        for length in range(1, len(s)):
            order += 26 ** length
        
        i = 0
        for char in s:
            char_index = ord(char) - 97
            order += char_index * (26 ** (len(s) - i - 1))
            i += 1
        
        return order + 1
    
    def order_to_string(order):
        length = 1
        total = 0
        while total + 26 ** length < order:
            total += 26 ** length
            length += 1
        
        index_in_length = order - total - 1
        
        result = ""
        for i in range(length):
            digit = index_in_length // (26 ** (length - i - 1))
            result += chr(ord('a') + digit)
            index_in_length %= (26 ** (length - i - 1))
        
        return result

    ban_orders = []
    for ban in bans:
        ban_orders.append(string_to_order(ban))
    ban_orders.sort()
    
    current_n = n
    for ban_order in ban_orders:
        if ban_order <= current_n:
            current_n += 1
        else:
            break
    
    return order_to_string(current_n)