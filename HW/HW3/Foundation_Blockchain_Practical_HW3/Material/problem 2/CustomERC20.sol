pragma solidity ^0.5.10;

import "browser/Safemath.sol";

contract CustomERC20 {
    using SafeMath for uint256;
    mapping (address => uint256) private _balances;
    mapping (address => mapping (address => uint256)) private _allowances;
    mapping (address => mapping(address => uint256)) private _allowancesExpireTime;

    uint256 private _totalSupply;

    event Transfer(address sender, address recipient, uint256 amount);
    event Approval(address owner, address spender, uint256 amount);
    event TimeApproval(address owner, address spender, uint256 expireTime);
    event Paused(address account);
    event Unpaused(address account);

    bool private _paused;
    address private _pauser;

    constructor () internal {
        _pauser = msg.sender;
        _totalSupply += 1000;
        _balances[msg.sender] += 1000;
    }
    
    // for this aim _paused event should be false
    modifier whenNotPaused() {
        require(!_paused);
        _;
    }

    /**
     * @dev Only Puaser.
     *
     * Checks whether msg.sender is pauser or not
     */
     
     // for this aim only _pauser can have access
    modifier onlyPauser() {
        require(msg.sender == _pauser);
        _;
    }

    /**
     * @dev Pause.
     *
     * Get contract pause status
     */
     
    function paused() public view returns (bool) {
        return _paused;
    }

    /**
     * @dev isPauser.
     *
     * Checks whether account is pauser or not
     */
     
    // just need to 
    function isPauser(address account) private view returns (bool) {
        return (account == _pauser);
    }

    /**
     * @dev Pause.
     *
     * Pauses contract all external and public functions
     *
     * Requirements:
     *
     * - the caller must be the pauser
     */
    function pause() public onlyPauser returns (bool) {
        _paused = true;
        emit Paused(msg.sender);
        return true;
    }

    /**
     * @dev Pause.
     *
     * Unpauses contract all external and publuic functions
     *
     * Requirements:
     *
     * - the caller must be the pauser
     */
    function unpause() public onlyPauser {
        require(_paused == true);
        _paused = false;
        emit Unpaused(msg.sender);
    }

    /**
     * @dev Returns the amount of tokens in existence.
     */
    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }

     /**
     * @dev Returns the amount of tokens owned by `account`.
     */
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev {ERC20-transfer}.
     *
     * Requirements:
     *
     * - `recipient` cannot be the zero address.
     * - the caller must have a balance of at least `amount`.
     */
    function transfer(address recipient, uint256 amount) public whenNotPaused returns (bool) {
         _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev {ERC20-allowance}.
     */
    function allowance(address owner, address spender) public view whenNotPaused returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev {ERC20-approve}.
     *
     * Requirements:
     *
     * - `spender` cannot be the zero address.
     */
    function approve(address spender, uint256 amount, uint expireTime) public whenNotPaused returns (bool) {
        if(expireTime == 0){
        _approve(msg.sender, spender, amount);
        }else{
            _approveExpireTime(msg.sender, spender,expireTime);
        }
        return true;
    }

    /**
     * @dev {ERC20-transferFrom}.
     *
     * Emits an {Approval} event indicating the updated allowance. This is not
     * required by the EIP. See the note at the beginning of {ERC20};
     *
     * Requirements:
     * - `sender` and `recipient` cannot be the zero address.
     * - `sender` must have a balance of at least `amount`.
     * - the caller must have allowance for `sender`'s tokens of at least
     * `amount`.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public whenNotPaused returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender].sub(amount, "ERC20: transfer amount exceeds allowance"));
        return true;
    }

    /**
     * @dev Moves tokens `amount` from `sender` to `recipient`.
     *
     * This is internal function is equivalent to {transfer}, and can be used to
     * e.g. implement automatic token fees, slashing mechanisms, etc.
     *
     * Emits a {Transfer} event.
     *
     * Requirements:
     *
     * - `sender` cannot be the zero address.
     * - `recipient` cannot be the zero address.
     * - `sender` must have a balance of at least `amount`.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        _balances[sender] = _balances[sender].sub(amount, "ERC20: transfer amount exceeds balance");
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Destroys `amount` tokens from `account`, reducing the
     * total supply.
     *
     * Emits a {Transfer} event with `to` set to the zero address.
     *
     * Requirements
     *
     * - `account` cannot be the zero address.
     * - `account` must have at least `amount` tokens.
     */
    function _burn(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: burn from the zero address");

        _balances[account] = _balances[account].sub(amount, "ERC20: burn amount exceeds balance");
        _totalSupply = _totalSupply.sub(amount);
        emit Transfer(account, address(0), amount);
    }

    /**
     * @dev Sets `amount` as the allowance of `spender` over the `owner`s tokens.
     *
     * This is internal function is equivalent to `approve`, and can be used to
     * e.g. set automatic allowances for certain subsystems, etc.
     *
     * Emits an {Approval} event.
     *
     * Requirements:
     *
     * - `owner` cannot be the zero address.
     * - `spender` cannot be the zero address.
     */
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @dev Sets `expire time` as the allowance of `spender` over the `owner`s tokens.
     *
     * Emits an {TimeApproval} event.
     *
     * Requirements:
     *
     * - `owner` cannot be the zero address.
     * - `spender` cannot be the zero address.
     */
    function _approveExpireTime(address owner, address spender, uint expireTime) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");
        emit TimeApproval(owner, spender, expireTime);
    }

    /** @dev Creates `amount` tokens and assigns them to `account`, increasing
     * the total supply.
     *
     * Emits a {Transfer} event with `from` set to the zero address.
     *
     * Requirements
     *
     * - `to` cannot be the zero address.
     */
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: mint to the zero address");

        _totalSupply = _totalSupply.add(amount);
        _balances[account] = _balances[account].add(amount);
        emit Transfer(address(0), account, amount);
    }

    /**
     * @dev Destroys `amount` tokens from `account`.`amount` is then deducted
     * from the caller's allowance.
     *
     * See {_burn} and {_approve}.
     */
    function _burnFrom(address account, uint256 amount) internal {
        _burn(account, amount);
        _approve(account, msg.sender, _allowances[account][msg.sender].sub(amount, "ERC20: burn amount exceeds allowance"));

    }
}