def test_deposit(context: AlgopyTestContext) -> None:
    #Arrange
    contract = PersonalBank
    app = context.ledger.get_app(contract)
    deposit_amount = context.any.uint64()
    deposit_txn = context.any.txn.payment(receiver=app.address, amount=deposit_amount)

    #Act
    output = contract.deposit(pay_txn=deposit_txn)

    #Assert
    assert output == deposit_amount