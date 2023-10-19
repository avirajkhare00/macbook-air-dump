# Lattice Protocol Architecture Blocks

 - ### p2p messaging
    We are using **WebRTC** protocol for file transfer, video call and audio call. Every file and every message is encrypted using ECIES with SHA256. It can only be decrypted by your private key. When you write a message, that message is encrypted and can only be decrypted by the specific receiving user's private key.
 - ### Reputation Engine
    Reputation of any ecosystem is weighted-average of their activities. Each and every activity has different weight. We will take all these weights and structure them in **JSON schema**, after structuring it, we will store it to **IPFS** network. We will store the **IPFS Hash** inside smart contract. To start with, our ethereum smart contracts will be computing all these weights. The average outcome of this gets stored on identity smart contract.
   - Example: [OpenBaazar Reputation Engine](https://www.openbazaar.org/blog/decentralized-reputation-in-openbazaar/)

 - ### Recommendation Engine
   We are using recommendation engine to give any business a recommendation to join any business. We are doing this using **tensorflow.js** library. Using this library, business can see their recommended ecosystem. Since AI will run on their client machine, business do not need to send any of their personal data in our backend. We will be storing modelling data on **IPFS**.

 - ### Data Permissioning
   We are using **Quorum** Blockchain for this task. Smart contract will take care of data permissioning between parties.
   
