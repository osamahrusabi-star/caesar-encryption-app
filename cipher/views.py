from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from caesar_cipher import caesar_encrypt, caesar_decrypt


def index(request):
    """Render the main page"""
    return render(request, 'index.html')


@csrf_exempt
def process(request):
    """Process encryption or decryption request"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', '')
            shift = int(data.get('shift', 0))
            operation = data.get('operation', 'encrypt')
            
            if operation == 'encrypt':
                result = caesar_encrypt(text, shift)
            else:
                result = caesar_decrypt(text, shift)
            
            return JsonResponse({
                'success': True,
                'result': result
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
