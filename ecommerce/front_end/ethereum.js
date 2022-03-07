import { ethers, Contract } from 'ethers';
import PaymentProcessor from './chain-info/contracts/PaymentProcessor.json';
import TestERC20 from './chain-info/contracts/TestERC20.json';
import networkMapping from './chain-info/deployments/map.json';

const getBlockchain = () =>
  new Promise((resolve, reject) => {
    window.addEventListener('load', async () => {
      if(window.ethereum) {
        await window.ethereum.enable();
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        // const signerAddress = await signer.getAddress();
        const networkId = '42';
        const PaymentProcessor_address =  networkMapping[String(networkId)]["PaymentProcessor"][0];
        const paymentProcessor = new Contract(
          PaymentProcessor_address,
          PaymentProcessor.abi,
          signer
        );
        const TestERC20_address =  networkMapping[String(networkId)]["TestERC20"][0];
        const TestToken = new Contract(
          TestERC20_address,
          TestERC20.abi,
          signer
        );

        resolve({provider, paymentProcessor, TestToken});
      }
      resolve({provider: undefined, paymentProcessor: undefined, TestToken: undefined});
    });
  });

export default getBlockchain;

