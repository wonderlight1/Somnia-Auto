import asyncio
import random
from loguru import logger
from web3 import Web3
from src.model.somnia_network.constants import SomniaProtocol
from src.utils.decorators import retry_async
from src.utils.constants import EXPLORER_URL_SOMNIA
from eth_account import Account
from src.model.onchain.web3_custom import Web3Custom


class Quills:
    def __init__(
        self, account_index: int, somnia_web3: Web3Custom, config: dict, wallet: Account
    ):
        self.account_index = account_index
        self.somnia_web3 = somnia_web3
        self.config = config
        self.wallet = wallet

    @retry_async(default_value=False)
    async def chat(self):
        try:
            random_message = random.choice(self.config.QUILLS.QUILLS_MESSAGES)
            logger.info(
                f"{self.account_index} | Sending message in Quills: {random_message}"
            )

            # Определение контракта и его ABI
            contract_address = "0x16f2fEc3bF691E1516B186F51e0DAA5114C9b5e8"
            contract_abi = [
                {
                    "inputs": [
                        {"internalType": "string", "name": "message", "type": "string"}
                    ],
                    "name": "addFun",
                    "outputs": [],
                    "stateMutability": "payable",
                    "type": "function",
                }
            ]

            # Создание контракта
            contract = self.somnia_web3.web3.eth.contract(
                address=self.somnia_web3.web3.to_checksum_address(contract_address),
                abi=contract_abi,
            )

            # Подготовка параметров для вызова функции addFun
            eth_value = Web3.to_wei(0.0001, "ether")  # 0.0001 ETH in wei

            # Создание вызова функции
            function_call = contract.functions.addFun(random_message)

            # Подготовка транзакции
            transaction = await function_call.build_transaction(
                {
                    "from": self.wallet.address,
                    "value": eth_value,
                    "nonce": await self.somnia_web3.web3.eth.get_transaction_count(
                        self.wallet.address
                    ),
                    "chainId": await self.somnia_web3.web3.eth.chain_id,
                }
            )

            # Получение газовых параметров
            gas_params = await self.somnia_web3.get_gas_params()
            transaction.update(gas_params)

            # Оценка газа с буфером
            gas_limit = await self.somnia_web3.estimate_gas(transaction)
            transaction["gas"] = gas_limit

            # Выполнение транзакции
            tx_hash = await self.somnia_web3.execute_transaction(
                transaction,
                self.wallet,
                await self.somnia_web3.web3.eth.chain_id,
                EXPLORER_URL_SOMNIA,
            )

            if tx_hash:
                logger.success(
                    f"{self.account_index} | Successfully sent message to Quills contract: {random_message}"
                )

            return True
        except Exception as e:
            random_sleep = random.randint(
                self.config.SETTINGS.PAUSE_BETWEEN_ATTEMPTS[0],
                self.config.SETTINGS.PAUSE_BETWEEN_ATTEMPTS[1],
            )
            logger.error(
                f"{self.account_index} | Error sending message in Quills: {e}. Sleeping for {random_sleep} seconds..."
            )
            await asyncio.sleep(random_sleep)
            return False
