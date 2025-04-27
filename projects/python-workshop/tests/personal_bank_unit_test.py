from collections.abc import Iterator
import pytest
from algopy_testing import AlgopyTestContext, algopy_testing_context
from smart_contracts.personal_bank.contract import PersonalBank

@pytest.fixture()
def context() -> Iterator[AlgopyTestContext]:
    with algopy_testing_context() as ctx:
        yield ctx


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