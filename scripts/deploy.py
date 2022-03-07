from scripts.helpful_scripts import (
    get_account,
    get_account_1,
)
from brownie import (
    TestERC20,
    PaymentProcessor,
    chain,
    config,
    network,
)
from web3 import Web3
import yaml
import json
import os
import shutil

initial_supply = Web3.toWei(1000000, "ether")
DECIMALS = 18


def update_front_end():
    # Send the build folder to the "chain-info" folder in the front_end src folder
    copy_folders_to_web_dev("./build", "./front_end/src/chain-info")

    # Sending our brownie config to the front end in JSON format
    # Install pip install pyyaml
    with open("brownie-config.yaml", "r") as brownie_config:
        config_dict = yaml.load(brownie_config, Loader=yaml.FullLoader)
        with open("./front_end/src/brownie-config.json", "w") as brownie_config_json:
            json.dump(config_dict, brownie_config_json)
    print("Front end updated!")


def update_back_end():
    # Send the build folder to the "chain-info" folder in the front_end src folder
    copy_folders_to_web_dev("./build", "./back_end/chain-info")

    # Sending our brownie config to the front end in JSON format
    # Install pip install pyyaml
    with open("brownie-config.yaml", "r") as brownie_config:
        config_dict = yaml.load(brownie_config, Loader=yaml.FullLoader)
        with open("./back_end/brownie-config.json", "w") as brownie_config_json:
            json.dump(config_dict, brownie_config_json)
    print("Back end updated!")


def copy_folders_to_web_dev(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def deploy_ERC20():
    account = get_account()
    test_token = TestERC20.deploy(initial_supply, {"from": account})
    print(test_token.name())


def deploy_PaymentProcessor():
    account = get_account()
    PaymentProcessor_contract = PaymentProcessor.deploy(
        account.address,
        TestERC20[-1],
        {"from": account},
    )
    print(PaymentProcessor_contract.address)


def test_PaymentProcessor():
    account = get_account()
    amount = Web3.toWei(1000, "ether")
    TestERC20[-1].approve(PaymentProcessor[-1], amount, {"from": account})
    tx = PaymentProcessor[-1].pay(amount, 1234, {"from": account})


def main():
    test_PaymentProcessor()
