function toggleButton() {
    if (!window.ethereum) {
      alert("MetaMask is not installed!");
      metamaskbtn.innerText = "Metamask not found";
      return false;
    }
    metamaskbtn.addEventListener("click", loginWithMetaMask);
  }
  async function loginWithMetaMask() {
    const accounts = await window.ethereum
      .request({ method: "eth_requestAccounts" })
      .catch((e) => {
        console.error(e.message);
        return;
      });
    if (!accounts) {
      return;
    }

    window.userWalletAddress = accounts[0];
    userWallet.innerText = window.userWalletAddress;
    metamaskbtn.innerText = "Sign out of MetaMask";

    metamaskbtn.removeEventListener("click", loginWithMetaMask);
    setTimeout(() => {
      metamaskbtn.addEventListener("click", signOutOfMetaMask);
    }, 200);
  }

  function signOutOfMetaMask() {
    window.userWalletAddress = null;
    userWallet.innerText = "";
    metamaskbtn.innerText = "Sign in with MetaMask";

    metamaskbtn.removeEventListener("click", signOutOfMetaMask);
    setTimeout(() => {
      metamaskbtn.addEventListener("click", loginWithMetaMask);
    }, 200);
  }

  window.addEventListener("DOMContentLoaded", () => {
    toggleButton();
  });