# Inicialize as listas vazias para armazenar compras, vendas e o estoque.
# Pode-se apenas ser vendido o que existe no estoque, potanto, o estoque inicial é 0.
# Recomenda-se se quiser fazer um estoque já existente e dái começar venda e compra,
# Primeiramente adiciona os itens no estoque com valor 0, dai passe a vende-los.
compras = []
vendas = []
estoque = []


def calcular_valor_total(quantidade, valor_unitario):
  return quantidade * valor_unitario


def centralizar_texto(texto, largura):
  return texto.center(largura)


def encontrar_item_estoque(nome_produto):
  for item in estoque:
    if item["produto"] == nome_produto:
      return item
  return None


def valor_total_compras():
  return sum([c["total"] for c in compras])


def valor_total_vendas():
  return sum([v["total"] for v in vendas])


def registrar_compra():
  nome_produto = input("Digite o nome do produto: ")
  while not nome_produto:
    print("Erro: Nome do produto não pode ser vazio.")
    nome_produto = input("Digite o nome do produto: ")

  quantidade = input("Digite a quantidade comprada: ")
  while not quantidade.isdigit():
    print("Erro: A quantidade deve ser um número inteiro.")
    quantidade = input("Digite a quantidade comprada: ")
  quantidade = int(quantidade)

  valor_unitario = input("Digite o valor unitário: ")
  while not valor_unitario.replace('.', '', 1).isdigit():
    print(
        "Erro: O valor unitário deve ser um número (use '.' como separador decimal)."
    )
    valor_unitario = input("Digite o valor unitário: ")
  valor_unitario = float(valor_unitario)

  valor_total = calcular_valor_total(quantidade, valor_unitario)
  compra = {
      "produto": nome_produto,
      "quantidade": quantidade,
      "valor_unitario": valor_unitario,
      "total": valor_total
  }
  compras.append(compra)

  # Atualiza o estoque
  item_estoque = encontrar_item_estoque(nome_produto)
  if item_estoque:
    item_estoque["quantidade"] += quantidade
  else:
    estoque.append({"produto": nome_produto, "quantidade": quantidade})

  print("Compra registrada com sucesso!")


def registrar_venda():
  nome_produto = input("Digite o nome do produto: ")
  while not nome_produto:
    print("Erro: Nome do produto não pode ser vazio.")
    nome_produto = input("Digite o nome do produto: ")

  quantidade = input("Digite a quantidade vendida: ")
  while not quantidade.isdigit():
    print("Erro: A quantidade deve ser um número inteiro.")
    quantidade = input("Digite a quantidade vendida: ")
  quantidade = int(quantidade)

  valor_unitario = input("Digite o valor unitário: ")
  while not valor_unitario.replace('.', '', 1).isdigit():
    print(
        "Erro: O valor unitário deve ser um número (use '.' como separador decimal)."
    )
    valor_unitario = input("Digite o valor unitário: ")
  valor_unitario = float(valor_unitario)

  # Verifica se o item existe no estoque
  item_estoque = encontrar_item_estoque(nome_produto)
  if not item_estoque:
    print(f"Erro: Produto {nome_produto} não encontrado no estoque.")
    return

  # Verifica se a quantidade vendida não é maior do que a quantidade em estoque
  if quantidade > item_estoque["quantidade"]:
    print(
        f"Erro: A quantidade disponível em estoque de {nome_produto} é menor do que a quantidade informada."
    )
    return

  valor_total = calcular_valor_total(quantidade, valor_unitario)
  venda = {
      "produto": nome_produto,
      "quantidade": quantidade,
      "valor_unitario": valor_unitario,
      "total": valor_total
  }
  vendas.append(venda)

  # Atualiza o estoque
  item_estoque["quantidade"] -= quantidade

  print("Venda registrada com sucesso!")


def verificar_saldo():
  total_compras = valor_total_compras()
  total_vendas = valor_total_vendas()
  lucro = total_vendas - total_compras
  print(f"\nSaldo total das vendas: R${lucro:.2f}")


def listar_compras():
  if not compras:
    print("Nenhuma compra registrada ainda.")
    return
  print("\nTabela de Compras:")
  print("{:<20} {:<12} {:<25} {:<20}".format("Produto", "Quantidade",
                                             "Valor Unitário", "Total"))
  for compra in compras:
    print("{:<20} {:<12} {:<25} {:<20}".format(
        compra['produto'], compra['quantidade'],
        f"R${compra['valor_unitario']:.2f}", f"R${compra['total']:.2f}"))
  print("{:<20} {:<12} {:<25} {:<20}".format("Total de Compras", "", "",
                                             f"R${valor_total_compras():.2f}"))


def listar_vendas():
  if not vendas:
    print("Nenhuma venda registrada ainda.")
    return
  print("\nTabela de Vendas:")
  print("{:<20} {:<12} {:<25} {:<20}".format("Produto", "Quantidade",
                                             "Valor Unitário", "Total"))
  for venda in vendas:
    print("{:<20} {:<12} {:<25} {:<20}".format(
        venda['produto'], venda['quantidade'],
        f"R${venda['valor_unitario']:.2f}", f"R${venda['total']:.2f}"))
  print("{:<20} {:<12} {:<25} {:<20}".format("Total de Vendas", "", "",
                                             f"R${valor_total_vendas():.2f}"))


def listar_estoque():
  if not estoque:
    print("Estoque vazio.")
    return
  print("\nTabela de Estoque:")
  print("{:<20} {:<12}".format("Produto", "Quantidade"))
  for item in estoque:
    print("{:<20} {:<12}".format(item['produto'], item['quantidade']))


while True:
  print("\nMenu de Opções:")
  print("1. Registrar uma compra")
  print("2. Registrar uma venda")
  print("3. Listar compras")
  print("4. Listar vendas")
  print("5. Lucro: Verificar o saldo total das vendas")
  print("6. Listar estoque")
  print("7. Sair do programa")

  opcao = input("Escolha uma opção (1/2/3/4/5/6/7): ")

  if opcao == "1":
    registrar_compra()
  elif opcao == "2":
    registrar_venda()
  elif opcao == "3":
    listar_compras()
  elif opcao == "4":
    listar_vendas()
  elif opcao == "5":
    verificar_saldo()
  elif opcao == "6":
    listar_estoque()
  elif opcao == "7":
    print("Encerrando o programa. Obrigado!")
    break
  else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
