from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


import random

def create_custom_seed(passphrase):
    # Generate a pseudo-random seed from the passphrase
    seed = 0
    for char in passphrase:
        seed = seed * 31 + ord(char)
    return seed

def encrypt(plaintext, passphrase):
    seed = create_custom_seed(passphrase)
    random.seed(seed)
    
    # Substitution: Shift characters only
    encrypted_text = ''
    shifts = []
    for char in plaintext:
        if char.isalpha():
            shift = random.randint(1, 25)
            shifts.append(shift)
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
            shifts.append(0)  # No shift for non-alphabet characters
    
    return encrypted_text


def decrypt(ciphertext, passphrase):
    seed = create_custom_seed(passphrase)
    random.seed(seed)
    
    # Generate shifts dynamically
    shifts = []
    for char in ciphertext:
        if char.isalpha():
            shift = random.randint(1, 25)
            shifts.append(shift)
        else:
            shifts.append(0)  # No shift for non-alphabet characters
    
    # Reverse Substitution using dynamically generated shifts
    decrypted_text = ''
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = shifts[i]
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char

    return decrypted_text


def result(request):
    return render(request, 'result.html')

def home(request):
    return render(request, 'home.html')


def process_fins(request):
    if request.method == 'POST':
        plaintext = request.POST.get('text')
        passphrase = request.POST.get('passphrase')
        operation = request.POST.get('operation')

        if operation == 'encryption':
            encrypted_text = encrypt(plaintext, passphrase)
            return render(request, 'result.html', {'result': encrypted_text, 'operation': 'Encryption'})
        elif operation == 'decryption':
            decrypted_text = decrypt(plaintext, passphrase)
            return render(request, 'result.html', {'result': decrypted_text, 'operation': 'Decryption'})

    return render(request, 'home.html')  # Render the HTML template for input

