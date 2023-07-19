# Assign Variables per original script
PADCNT = 7
PAD0 = "ohfyAeiXNOCYz2HF4GrV97Ua01Bk5DMWpIlsJtgc8ujZLTqPwvKRxnSmQ3Ed6b"
PAD1 = "TPl1Q5tghW3pS6mcRdufHIK47LECkqiynB82ADazjxOMoZeVGsU9XJrNbwFvY0"
PAD2 = "TQhoui3JqMIG2pAgUv9jOaScZmYDnNedb5WBV6FHftrLy48wzk1KlRP0Cxs7EX"
PAD3 = "by6Z4o2t0LJiKVFqMuwDaNRjrmvOHp1U3BYI9GfkA7cgeExXCPsWdnlShzQ85T"
PAD4 = "bfsoW1tEvdk47MZGCeOAqp3nrKjH8xLwlPJgTS902NauicIQU5hV6BRzyFYDmX"
PAD5 = "acPlFoX1Gt2byEeU5DKix6guTCAvHqdYkJBmQprSZVL8n9fIj3WOw7RNz40hMs"
PAD6 = "s2FUhEeYwO1cX0WniLdqbKfjgA9GyVNQuzoBtZlrSDP7J83kTvIC65xpRMHam4"

# Assign MdstPad variable per original script
MdstPad = ["ohfyAeiXNOCYz2HF4GrV97Ua01Bk5DMWpIlsJtgc8ujZLTqPwvKRxnSmQ3Ed6b", "TPl1Q5tghW3pS6mcRdufHIK47LECkqiynB82ADazjxOMoZeVGsU9XJrNbwFvY0", "TQhoui3JqMIG2pAgUv9jOaScZmYDnNedb5WBV6FHftrLy48wzk1KlRP0Cxs7EX", "by6Z4o2t0LJiKVFqMuwDaNRjrmvOHp1U3BYI9GfkA7cgeExXCPsWdnlShzQ85T", "bfsoW1tEvdk47MZGCeOAqp3nrKjH8xLwlPJgTS902NauicIQU5hV6BRzyFYDmX", "acPlFoX1Gt2byEeU5DKix6guTCAvHqdYkJBmQprSZVL8n9fIj3WOw7RNz40hMs", "s2FUhEeYwO1cX0WniLdqbKfjgA9GyVNQuzoBtZlrSDP7J83kTvIC65xpRMHam4"]

def MdstEncrypt(source):
    idx = 0
    destBuf = source
    # Assigns padidx to the remainer when the length of source is divided by 7
    padidx = len(source) % 7
    # Assigns padstep to 1 if the remainder is odd and 6 if the remainder is even
    if padidx % 2 > 0:
        padstep = 1
    else:
        padstep = 6
    # Loops for the length of source double check this and at idx + 1
    while idx < len(source):
        # Assigns ch to the char at the current working index
        ch = source[idx]
        # Assigns ch per the rules defined in original script
        if ch.isnumeric():
            ch = MdstPad[padidx][int(ch)]
        elif ch.isupper():
            ch = MdstPad[padidx][ord(ch) - ord('A') + 10]
        elif ch.islower():
            ch = MdstPad[padidx][ord(ch) - ord('a') + 36]
        destBuf = destBuf[: idx] + ch + destBuf[idx + 1:]
        padidx = (padidx + padstep) % 7
        idx = idx + 1
    print(destBuf)
    return destBuf


def MdstDecrypt(source):
    idx = 0
    destBuf = source
    # Assigns padidx to the remainer when the length of source is divided by 7
    padidx = len(source) % 7
    # Assigns padstep to 1 if the remainder is odd and 6 if the remainder is even
    if padidx % 2 > 0:
        padstep = 1
    else:
        padstep = 6
    # Loops for the length of source double check this and at idx + 1
    while idx < len(source):
        # Assigns ch to the char at the current working index
        ch = source[idx]
        pos = MdstPad[padidx].index(ch)
        # Assigns ch per the rules defined in original script
        if pos > -1:
            if pos < 10:
                ch = chr(pos + 48)
            elif pos < 36:
                ch = chr(pos - 10 + 65)
            else:
                ch = chr(pos - 36 + 97)

        destBuf = destBuf[: idx] + ch + destBuf[idx + 1:]
        padidx = (padidx + padstep) % 7
        idx = idx + 1
    print(destBuf)
    return destBuf










MdstEncrypt("1")
MdstDecrypt("7")



