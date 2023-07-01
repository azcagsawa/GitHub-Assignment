#!/usr/bin/env python
# coding: utf-8

# In[36]:


def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    letter = letter.upper()
    
    abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    space = " "
    
    if letter in space:
        print(space)
    else:
        new = abc.index(letter) + shift
        if new >= len(abc):
            wrapped = new - len(abc)
            return abc[wrapped]
        else: 
            return abc[new]


# In[37]:


shift_letter("Y",2)


# In[38]:


def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    message = message.upper()
    
    msg_split = list(message)
    msg = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    boop = " "
    coded = ""
    
    for each in msg_split:
        if each in boop:
            coded += boop
        else:
            new = msg.index(each) + shift
            if new >= len(msg):
                wrapped = new - len(msg)
                coded += msg[wrapped]
            else:
                coded += msg[new]
    
    return coded


# In[39]:


caesar_cipher("QEFP FP TLOHFKD",3)


# In[50]:


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    letter = letter.upper()
    letter_shift = letter_shift.upper()
    
    basis = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    blank = " "
    
    if letter in blank: 
        return space
    else:
        equi = basis.index(letter) + basis.index(letter_shift)
        if equi >= len(basis):
            over = equi - len(basis)
            return basis[over]
        else:
            return basis[equi]


# In[52]:


shift_by_letter("J","Z")


# In[54]:


def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    
    # check if equal len of message and key
    # if unequal, make equal
    # once equal, identify the index of each letter in key based on "code"
    # if space: append a space to final code
    # if letter: equal index in key & message, shift message based on key's index
    
    message = message.upper()
    key = key.upper()
    
    code = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    blnk = " "
    secret = ""
    holder_key = [key]
    new_key = "".join(holder_key)
    
    # 1. making a new key (if necessary)
    
    while len (message) > len(new_key):
        for char in key:
            if len(message) > len(new_key):
                holder_key.append(char)
                new_key = "".join(holder_key)  
       
    # 2. shifting the message based on the index of its corresponding key
    
    for every_index in range(len(message)): 
        every = message[every_index]
        
        if every in blnk:
            secret += every
            
        else:                   
            corresponding_key = new_key[every_index] 
            code_index = code.index(corresponding_key) + code.index(every)
            if code_index >= len(code):
                code_index = code_index - len(code)
                secret += code[code_index]
            else: 
                secret += code[code_index]            
    
    return secret


# In[55]:


vigenere_cipher("A C", "KEY")


# In[56]:


def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift. 
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    ref = list(message)
    message_holder = [message]
    new_message = "".join(message_holder)   
    encrypted_message = ""
    
    # 1. check if len(message) is a multiple of the shift 
    
    while len(new_message) % shift != 0:
        message_holder = [message]
        for each_letter in message:
            if len(new_message) % shift != 0:
                message_holder.append("_")
                new_message = "".join(message_holder)    
            else:
                break
                
    new_message = "".join(message_holder)            
    
    for each_index in range(len(message)):
        each = message[each_index]
        trial = (each_index // shift) + len(new_message) // shift * (each_index % shift)
        found_letter = ref[trial]
        encrypted_message += found_letter
        
    return encrypted_message


# In[57]:


scytale_cipher("ALGORITHMS_ARE_IMPORTANT",8)


# In[58]:


def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    reference = list(message)
    message_container = [message]
    adjusted_message = "".join(message_container)
    decrypted_message = ""
    
    while len(adjusted_message) % shift != 0:
        message_container = [message]
        for each_char in message:
            if len(adjusted_message) % shift != 0:
                message_container.append("_")
                adjusted_message = "".join(message_container)    
            else:
                break
                
    adjusted_message = "".join(message_container)  
    message = adjusted_message
    
    for ea_num in range(0,shift):
        holder = ""
        counter = 0
        while len(holder) != len(message) // shift:
            decrypted_message += message[ea_num + counter]
            holder += message[ea_num + counter]
            counter += shift        
        
    return decrypted_message


# In[59]:


scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8)


# In[ ]:





# In[ ]:




