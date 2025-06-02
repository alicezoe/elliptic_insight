The Elliptic Dataset is a graph network of Bitcoin transactions with handcrafted features. 
All features are constructed using only publicly available information.

The Elliptic DataSet maps Bitcoin transactions to real entities in two categories:

Licit: exchanges, wallet providers, miners, licit services, etc.
Ilicit: scams, malware, terrorist, organization, ransomware, Ponzi shcemes, etc

A given transaction is licit if the entity that generated it was licit.

Nodes and Edges 203,769 node transactions and 234,355 directed edge payments flows. 2% are ilicit (Class 1), 21% are licit (Class 2)
Features Each node has associated 166 features. 94 represent local information (timestep, number of inputs/outputs, transaction fee, output volume and aggregated figures) and 72 features represent aggregated features (obtained by aggregating transaction information such as maximum, minimum, standard deviation, correlation coefficients of neighbor transactions).
Temporal Information A time step is associated with each node, representing an stimated of the time when the transaction is confirmed. There are 49 distinct timesteps evenly spaced with an interval of 2 weeks.
