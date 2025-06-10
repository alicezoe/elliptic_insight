## Elliptic Dataset

The Elliptic Dataset is a large, publicly available graph-based dataset designed for research on detecting illicit activity in the Bitcoin blockchain. <br>It enables the study of anti-money laundering (AML), fraud detection, and financial forensics using machine learning and graph analysis techniques.

The Elliptic Dataset maps Bitcoin transactions to real entities in 2 categories:

1. Licit (class-2): exchanges, wallet providers, miners, licit services, etc.
2. Ilicit (class-1): scams, malware, terrorist, organization, ransomware, Ponzi schemes, etc.

Nodes (transactions) - 203,769
<br>Edges (money flow) - 234,355
<br>Time steps - 49
<br>Illicit (class-1) - 4,545
<br>Licit (class-2) - 42,019
<br>Unknown (class-3) - 157,205
<br>Features - 167

An "edge" represents a flow of Bitcoin between two transactions. <br>Specifically, the data set is structured as a transaction graph where:
- Each node corresponds to a Bitcoin transaction.
- Each edge indicates that Bitcoin value has moved from one transaction to another, effectively capturing the transfer of funds on the blockchain

This means an edge connects two transactions, showing the direction and presence of a payment or transfer. The edges are directed, signifying the direction of Bitcoin flow—from the source transaction to the destination transaction
