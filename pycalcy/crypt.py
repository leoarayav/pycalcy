'''
This is the module for the encryption who contains different types 
of encryption like hexdigest, byte manipulation and binary issues
you can use this module to encrypt your data and make it more secure
or simple convert it to a different type of data as you want

Author: Leo Araya (https://www.github.com/leoarayav)
'''

from typing import Union

class Encrypt:
    """The Encrypt class contains various methods for encryption"""

    def bit_move(self, data: Union[int, str], move: int) -> int:
        """
        Bitwise move the data to the left or right

        Args:
            data (Union[int, str]): The data to move
            move (int): The number of bits to move
        
        Returns:
            int: The data moved
        """
        if isinstance(data, str):
            data = int(data, 2)
        return data << move
    
    def bit_xor(self, data: Union[int, str], xor: int) -> int:
        """
        Bitwise XOR the data with a number

        Args:
            data (Union[int, str]): The data to XOR
            xor (int): The number to XOR
        
        Returns:
            int: The data XORed
        """
        if isinstance(data, str):
            data = int(data, 2)
        return data ^ xor
    
    def bit_and(self, data: Union[int, str], and_: int) -> int:
        """
        Bitwise AND the data with a number

        Args:
            data (Union[int, str]): The data to AND
            and_ (int): The number to AND
        
        Returns:
            int: The data ANDed
        """
        if isinstance(data, str):
            data = int(data, 2)
        return data & and_
    
    def rotate_left(self, data: int, rotate: int) -> int:
        """
        Rotates a 32-bit integer left

        Args:
            data (int): The data to rotate
            rotate (int): The number of bits to rotate
        
        Returns:
            int: The data rotated
        """
        return (data << rotate) | (data >> (32 - rotate))
    
    def rotate_right(self, data: int, rotate: int) -> int:
        """
        Rotates a 32-bit integer right

        Args:
            data (int): The data to rotate
            rotate (int): The number of bits to rotate
        
        Returns:
            int: The data rotated
        """
        return (data >> rotate) | (data << (32 - rotate))
    
    def hex_to_binary(self, data: str) -> str:
        """
        Convert hexadecimal to binary

        Args:
            data (str): The data to convert
        
        Returns:
            str: The data converted
        """
        return bin(int(data, 16))[2:]
    
    def binary_to_hex(self, data: str) -> str:
        """
            Convert binary to hexadecimal

            Args:
                data (str): The data to convert
            
            Returns:
                str: The data converted
        """
        return hex(int(data, 2))[2:]
    
    def hex_to_int(self, data: str) -> int:
        """
        Convert hexadecimal to integer

        Args:
            data (str): The data to convert

        Returns:
            int: The data converted
        """
        return int(data, 16)
    
    def int_to_hex(self, data: int) -> str:
        """
        Convert integer to hexadecimal

        Args:
            data (int): The data to convert
        
        Returns:
            str: The data converted
        """
        return hex(data)[2:]
    
    def bit_rotate_left(self, data: str, rotate: int) -> str:
        """
        Bitwise rotate left the data

        Args:
            data (str): The data to rotate
            rotate (int): The number of bits to rotate
        
        Returns:
            str: The data rotated
        """
        return bin(self.rotate_left(int(data, 2), rotate))[2:]
    
    def encrypt_text_to_hex(self, text: str) -> str:
        """
        Encrypt text with a key from scratch

        Args:
            text (str): The text to encrypt
        
        Returns:
            str: The text encrypted
        """
        key = 0
        for char in text:
            key += ord(char)
        return hex(key)[2:]
    
    def encrypt_text_to_binary(self, text: str) -> str:
        """
        Encrypt text with a key from scratch

        Args:
            text (str): The text to encrypt
        
        Returns:
            str: The text encrypted
        """
        key = 0
        for char in text:
            key += ord(char)
        return bin(key)[2:]
    
    def padding_byte(self, data: str) -> str:
        """
        Padding the data to 8 bits

        Args:
            data (str): The data to padding
        
        Returns:
            str: The data padded
        """
        return '0' * (8 - len(data)) + data
    
    def padding_hex(self, data: str) -> str:
        """
        Padding the data to 2 bytes

        Args:
            data (str): The data to padding
        
        Returns:
            str: The data padded
        """
        return '0' * (2 - len(data)) + data
    
    def padding_binary(self, data: str) -> str:
        """
        Padding the data to 8 bytes

        Args:
            data (str): The data to padding

        Returns:
            str: The data padded
        """
        return '0' * (8 - len(data)) + data