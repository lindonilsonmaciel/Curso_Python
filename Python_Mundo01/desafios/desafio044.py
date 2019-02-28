"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento: - à vista
dinheiro/cheque: 10% de desconto - à vista no cartão: 5% de desconto -
em até 2x no cartão: preço formal - 3x ou mais no cartão: 20% de juros"""
print('='*10,' LOJAS MACIEL ', '='*10)
preco = float(input('Preço final das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('>>> '))
if opcao == 1:
    print('O valor pago R$ {:.2f} à vista/cheque tem 10% de desconto, novo valor será R$ {:.2f}'.format(preco, preco-(preco*0.10)))
elif opcao == 2:
    print('O valor R$ {} à vista no cartão tem 5% de desconto, o novo valor fica R$ {}'.format(preco, preco-(preco*0.05)))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(preco/2))
else:
    print('Sua compra será parcelada em 3x e terá acréscimo de 20%(Novo preço R$ {:.2f}), as parcelas com acréscimo ficam em 3x de R$ {:.2f}'.format(preco+(preco*0.2),(preco + (preco * 0.2))/3))