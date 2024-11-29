from itertools import combinations
from django.http import JsonResponse
from django.shortcuts import render
from .models import Sorteio

def verificar_combinacoes(request):
    if request.method == "POST":
        # Obter o número de dezenas
        quantidade_dezenas = request.POST.get('quantidade_dezenas')

        # Obter as dezenas digitadas (podem estar no campo 'numeros', e podem ser múltiplos valores)
        numeros = request.POST.getlist('numeros')

        # Imprimir no terminal os números
        print(f"Quantidade de dezenas: {quantidade_dezenas}")
        print(f"Números digitados: {numeros}")

        # Aqui você pode adicionar lógica adicional para verificar combinações, se necessário

        # Retornar uma resposta JSON com o status ou dados
        return JsonResponse({
            'combinacoes_nao_encontradas': numeros  # Exemplo, você pode enviar o que for necessário
        })
    
    # Caso não seja um POST, apenas renderiza a página com o formulário
    return render(request, 'megasena/formulario.html')