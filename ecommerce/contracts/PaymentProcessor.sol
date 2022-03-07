pragma solidity >=0.6.6;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract PaymentProcessor {
    address public admin;
    IERC20 public TestToken;

    event PaymentDone(
        address payer,
        uint256 amount,
        uint256 paymentId,
        uint256 date
    );

    constructor(address adminAddress, address TestToken_Address) public {
        admin = adminAddress;
        TestToken = IERC20(TestToken_Address);
    }

    function pay(uint256 amount, uint256 paymentId) external {
        TestToken.transferFrom(msg.sender, admin, amount);
        emit PaymentDone(msg.sender, amount, paymentId, block.timestamp);
    }
}
