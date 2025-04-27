
import pytest

from algokit_utils import (
    AlgoAmount, 
    AlgorandClient, 
    CommonAppCallParams, 
    PaymentParams, 
    SendParams, 
    SigningAccount,
    )

from smart_contracts.artifacts.personal_bank.personal_bank_client import (
    DepositArgs, 
    PersonalBankClient, 
    PersonalBankFactory,
    )

@pytest.fixture(scope="session")
def deployer(algorand_client: AlgorandClient) -> SigningAccount:
    account = algorand_client.account.from_environment("DEPLOYER")
    algorand_client.account.ensure_funded_from_environment(
        account_to_fund=account.address, min_spending_balance=AlgoAmount.from_algo(10)
    )
    return account


@pytest.fixture(scope="session")
def depositor(algorand_client: AlgorandClient) -> SigningAccount:
    account = algorand_client.account.from_environment("DEPOSITOR")
    algorand_client.account.ensure_funded_from_environment(
        account_to_fund=account.address, min_spending_balance=AlgoAmount.from_algo(10)
    )
    return account