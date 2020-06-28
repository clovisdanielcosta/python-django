from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello: {} que tem {} anos</h1>'.format(nome, idade))

def soma(request, a, b):
    resultado = a + b
    operacao = 'Soma'
    return HttpResponse('<h1>A operação de {} de {} e {} é: {}.</h1>'.format(operacao, a, b, resultado))

def subtracao(request, a, b):
    resultado = a - b
    operacao = 'Subtração'
    return HttpResponse('<h1>A operação de {} de {} e {} é: {}.</h1>'.format(operacao, a, b, resultado))

def multiplicacao(request, a, b):
    resultado = a * b
    operacao = 'Multiplicação'
    return HttpResponse('<h1>A operação de {} de {} e {} é: {}.</h1>'.format(operacao, a, b, resultado))

def divisao(request, a, b):
    resultado = a / b
    operacao = 'Divisão'
    return HttpResponse('<h1>A operação de {} de {} e {} é: {}.</h1>'.format(operacao, a, b, resultado))
